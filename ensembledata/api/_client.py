from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Sequence

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

from ._requester import Requester

if TYPE_CHECKING:
    from ._response import EDResponse


class EDCustomer:
    def __init__(self, requester: Requester):
        self.requester = requester

    def get_usage(self, date: str, extra_params: dict[str, Any] | None = None) -> EDResponse:
        params = {"date": date}
        if extra_params is not None:
            params.update(extra_params)

        return self.requester.get(
            "/customer/get-used-units",
            params=params,
        )


class EDTikTok:
    def __init__(self, requester: Requester):
        self.requester = requester

    def hashtag_search(
        self, *, hashtag: str, cursor: int, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {"name": hashtag, "cursor": cursor}
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get(
            "/tt/hashtag/posts",
            params=params,
        )

    def full_hashtag_search(
        self,
        *,
        hashtag: str,
        days: int,
        max_cursor: int | None = None,
        remap_output: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "name": hashtag,
            "days": days,
        }
        if max_cursor is not None:
            params["max_cursor"] = max_cursor
        if remap_output is not None:
            params["remap_output"] = remap_output
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/tt/hashtag/recent-posts", params=params)

    def keyword_search(
        self,
        *,
        keyword: str,
        cursor: int,
        period: Literal["0", "1", "7", "30", "90", "180"],
        sorting: Literal["0", "1"],
        country: str | None = None,
        match_exactly: bool | None = None,
        get_author_stats: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "name": keyword,
            "cursor": cursor,
            "period": period,
            "sorting": sorting,
        }
        if country is not None:
            params["country"] = country
        if match_exactly is not None:
            params["match_exactly"] = match_exactly
        if get_author_stats is not None:
            params["get_author_stats"] = get_author_stats
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/tt/keyword/search", params=params)

    def full_keyword_search(
        self,
        *,
        keyword: str,
        period: Literal["0", "1", "7", "30", "90", "180"],
        sorting: Literal["0", "1"] | None = None,
        country: str | None = None,
        match_exactly: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": keyword,
            "period": period,
        }
        if sorting is not None:
            params["sorting"] = sorting
        if country is not None:
            params["country"] = country
        if match_exactly is not None:
            params["match_exactly"] = match_exactly
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/tt/keyword/full-search", params=params)

    def user_posts_from_username(
        self,
        username: str,
        *,
        depth: int,
        cursor: int | None = None,
        oldest_createtime: int | None = None,
        alternative_method: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "username": username,
            "depth": depth,
        }
        if cursor is not None:
            params["start_cursor"] = cursor
        if oldest_createtime is not None:
            params["oldest_createtime"] = oldest_createtime
        if alternative_method is not None:
            params["alternative_method"] = alternative_method
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/tt/user/posts", params=params, return_top_level_data=True)

    def user_posts_from_secuid(
        self,
        sec_uid: str,
        *,
        depth: int,
        cursor: int | None = None,
        oldest_createtime: int | None = None,
        alternative_method: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "secUid": sec_uid,
            "depth": depth,
        }
        if cursor is not None:
            params["start_cursor"] = cursor
        if oldest_createtime is not None:
            params["oldest_createtime"] = oldest_createtime
        if alternative_method is not None:
            params["alternative_method"] = alternative_method
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get(
            "/tt/user/posts-from-secuid", params=params, return_top_level_data=True
        )

    def user_info_from_username(
        self, username: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/user/info", params=params)

    def user_info_from_secuid(
        self,
        sec_uid: str,
        *,
        alternative_method: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "secUid": sec_uid,
        }
        if alternative_method is not None:
            params["alternative_method"] = alternative_method
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/tt/user/info-from-secuid", params=params)

    def user_search(
        self, *, keyword: str, cursor: int, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "keyword": keyword,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/user/search", params=params)

    def post_info(self, *, url: str, extra_params: dict[str, Any] | None = None) -> EDResponse:
        # TODO: allow awemeid as param?
        params = {
            "url": url,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/post/info", params=params)

    def multi_post_info(
        self, *, post_ids: Sequence[str], extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "ids": ";".join(post_ids),
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/post/multi-info", params=params)

    def post_comments(
        self,
        *,
        aweme_id: str,
        cursor: int | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "aweme_id": aweme_id,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/post/comments", params=params)

    def post_comment_replies(
        self,
        *,
        aweme_id: str,
        comment_id: str,
        cursor: int | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "aweme_id": aweme_id,
            "comment_id": comment_id,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/post/comments-replies", params=params)

    def music_search(
        self,
        *,
        keyword: str,
        cursor: int | None = None,
        sorting: Literal["0", "1", "2", "3", "4"],
        filter_by: Literal["0", "1", "2"],
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": keyword,
            "sorting": sorting,
            "filter_by": filter_by,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/music/info", params=params)

    def music_posts(
        self,
        *,
        music_id: str,
        cursor: int | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": music_id,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/music/posts", params=params)

    def music_details(
        self, *, music_id: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "id": music_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/music/details", params=params)

    def user_followers(
        self,
        *,
        id: str,
        sec_uid: str,
        cursor: int | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "secUid": sec_uid,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/user/followers", params=params)

    def user_followings(
        self,
        *,
        id: str,
        sec_uid: str,
        cursor: int | None = None,
        page_token: str | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "secUid": sec_uid,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if page_token is not None:
            params["page_token"] = page_token
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/user/followings", params=params)

    def user_liked_posts(
        self, *, sec_uid: str, cursor: int | None = None, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params: dict[str, Any] = {
            "secUid": sec_uid,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/tt/user/liked-posts", params=params)


class EDReddit:
    def __init__(self, requester: Requester):
        self.requester = requester

    def subreddit_posts(
        self,
        *,
        name: str,
        sort: Literal["hot", "new", "top", "rising"],
        period: Literal["hour", "day", "week", "month", "year", "all"],
        cursor: str,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "name": name,
            "sort": sort,
            "period": period,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/reddit/subreddit/posts", params=params)

    def post_comments(
        self, *, id: str, cursor: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "id": id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/reddit/post/comments", params=params)


class EDTwitch:
    def __init__(self, requester: Requester):
        self.requester = requester

    def keyword_search(
        self,
        *,
        keyword: str,
        depth: int,
        type: Literal["videos", "channels", "games"],
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "keyword": keyword,
            "depth": depth,
            "type": type,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/twitch/search", params=params)

    def user_followers(
        self, *, username: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/twitch/user/followers", params=params)


class EDInstagram:
    def __init__(self, requester: Requester):
        self.requester = requester

    def user_posts(
        self,
        *,
        user_id: int,
        depth: int,
        oldest_timestamp: int | None = None,
        chunk_size: int | None = None,
        cursor: str | None = None,
        alternative_method: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
            "depth": depth,
        }
        if oldest_timestamp is not None:
            params["oldest_timestamp"] = oldest_timestamp
        if chunk_size is not None:
            params["chunk_size"] = chunk_size
        if cursor is not None:
            params["start_cursor"] = cursor
        if alternative_method is not None:
            params["alternative_method"] = alternative_method
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/instagram/user/posts", params=params)

    def user_basic_stats(
        self, *, user_id: int, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "user_id": user_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/instagram/user/basic-info", params=params)

    def user_info(self, *, username: str, extra_params: dict[str, Any] | None = None) -> EDResponse:
        params = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/instagram/user/info", params=params)

    def user_detailed_info(
        self, *, username: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/instagram/user/detailed-info", params=params)

    def user_followers(
        self, *, user_id: int, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "user_id": user_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/instagram/user/followers", params=params)

    def user_reels(
        self,
        *,
        user_id: int,
        depth: int,
        include_feed_video: bool | None = None,
        oldest_timestamp: int | None = None,
        cursor: str | None = None,
        chunk_size: int | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
            "depth": depth,
        }
        if include_feed_video is not None:
            params["include_feed_video"] = include_feed_video
        if oldest_timestamp is not None:
            params["oldest_timestamp"] = oldest_timestamp
        if cursor is not None:
            params["start_cursor"] = cursor
        if chunk_size is not None:
            params["chunk_size"] = chunk_size
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/instagram/user/reels", params=params)

    def user_tagged_posts(
        self,
        *,
        user_id: int,
        cursor: str | None = None,
        chunk_size: int | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if chunk_size is not None:
            params["chunk_size"] = chunk_size
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/instagram/user/tagged-posts", params=params)

    def post_info_and_comments(
        self,
        *,
        code: str,
        num_comments: int | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "code": code,
        }
        if num_comments is not None:
            params["n_comments_to_fetch"] = num_comments
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/instagram/post/details", params=params)

    def hashtag_posts(
        self,
        *,
        hashtag: str,
        cursor: str | None = None,
        chunk_size: int | None = None,
        get_author_info: bool | None = None,
        alternative_method: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": hashtag,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if chunk_size is not None:
            params["chunk_size"] = chunk_size
        if get_author_info is not None:
            params["get_author_info"] = get_author_info
        if alternative_method is not None:
            params["alternative_method"] = alternative_method
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/instagram/hashtag/posts", params=params)

    def music_posts(
        self,
        *,
        music_id: str,
        cursor: str | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "id": music_id,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/instagram/music/posts", params=params)

    def search(self, *, text: str, extra_params: dict[str, Any] | None = None) -> EDResponse:
        params = {
            "text": text,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/instagram/search", params=params)


class EDYoutube:
    def __init__(self, requester: Requester):
        self.requester = requester

    def keyword_search(
        self,
        *,
        keyword: str,
        depth: int,
        cursor: str | None = None,
        period: Literal["overall", "hour", "today", "week", "month", "year"] | None = None,
        sorting: Literal["relevance", "time", "views", "rating"] | None = None,
        get_additional_info: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "keyword": keyword,
            "depth": depth,
        }
        if cursor is not None:
            params["start_cursor"] = cursor
        if period is not None:
            params["period"] = period
        if sorting is not None:
            params["sorting"] = sorting
        if get_additional_info is not None:
            params["get_additional_info"] = get_additional_info
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/youtube/search", params=params)

    def featured_category_search(
        self, *, keyword: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "name": keyword,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get(
            "/youtube/search/featured-categories",
            params=params,
        )

    def hashtag_search(
        self,
        *,
        hashtag: str,
        depth: int,
        only_shorts: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params = {
            "name": hashtag,
            "depth": depth,
        }
        if only_shorts is not None:
            params["only_shorts"] = only_shorts
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/youtube/hashtag/search", params=params)

    def channel_detailed_info(
        self,
        channel_id: str,
        *,
        from_url: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
        }
        if from_url is not None:
            params["from_url"] = from_url
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/youtube/channel/detailed-info", params=params)

    def channel_videos(
        self, channel_id: str, *, depth: int, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "browseId": channel_id,
            "depth": depth,
        }
        if extra_params is not None:
            params.update(extra_params)
        return self.requester.get("/youtube/channel/videos", params=params)

    def channel_shorts(
        self, channel_id: str, *, depth: int, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "browseId": channel_id,
            "depth": depth,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/youtube/channel/shorts", params=params)

    def video_or_short_details(
        self,
        *,
        id: str,
        alternative_method: bool | None = None,
        get_subscribers_count: bool | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
        }
        if alternative_method is not None:
            params["alternative_method"] = alternative_method
        if get_subscribers_count is not None:
            params["get_subscribers_count"] = get_subscribers_count
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get(
            "/youtube/channel/get-short-stats",
            params=params,
        )

    def channel_subscribers(
        self, channel_id: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "browseId": channel_id,
        }
        if extra_params is not None:
            params.update(extra_params)
        return self.requester.get("/youtube/channel/followers", params=params)

    def channel_username_to_id(
        self, username: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "name": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/youtube/channel/name-to-id", params=params)

    def channel_id_to_username(
        self, channel_id: str, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "browserId": channel_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/youtube/channel/id-to-name", params=params)

    def music_id_to_shorts(
        self,
        *,
        music_id: str,
        depth: int | None = None,
        extra_params: dict[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": music_id,
        }
        if depth is not None:
            params["depth"] = depth
        if extra_params is not None:
            params = {**extra_params, **params}

        return self.requester.get("/youtube/music/id-to-shorts", params=params)

    def video_comments(
        self, *, id: str, cursor: str | None = None, extra_params: dict[str, Any] | None = None
    ) -> EDResponse:
        params = {
            "id": id,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if extra_params is not None:
            params = {**extra_params, **params}
        return self.requester.get("/youtube/video/comments", params=params)


class EDClient:
    def __init__(self, token: str, *, timeout: int = 600, max_network_retries: int = 3):
        self.requester = Requester(token, timeout=timeout, max_network_retries=max_network_retries)
        self.customer = EDCustomer(self.requester)
        self.tiktok = EDTikTok(self.requester)
        self.instagram = EDInstagram(self.requester)
        self.youtube = EDYoutube(self.requester)
        self.reddit = EDReddit(self.requester)
        self.twitch = EDTwitch(self.requester)

    def request(self, uri: str, params: dict[str, Any] | None = None) -> EDResponse:
        return self.requester.get(uri, params=params or {})
