from __future__ import annotations

from typing import Sequence

from typing_extensions import Literal

from .requester import Requester


class EDCustomer:
    def __init__(self, requester: Requester):
        self.requester = requester

    def get_usage(self, date: str, **kwargs):
        return self.requester.get(
            "/customer/get-used-units",
            params={"date": date, **kwargs},
        )


class EDTikTok:
    def __init__(self, requester: Requester):
        self.requester = requester

    def hashtag_search(self, *, hashtag: str, cursor: int, **kwargs):
        return self.requester.get(
            "/tt/hashtag/posts",
            params={"name": hashtag, "cursor": cursor, **kwargs},
        )

    def full_hashtag_search(
        self,
        *,
        hashtag: str,
        days: int,
        max_cursor: int | None = None,
        remap_output: bool | None = None,
    ):
        params = {
            "name": hashtag,
            "days": days,
        }
        if max_cursor is not None:
            params["max_cursor"] = max_cursor
        if remap_output is not None:
            params["remap_output"] = remap_output

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
        **kwargs,
    ):
        params = {
            "keyword": keyword,
            "cursor": cursor,
            "period": period,
            "sorting": sorting,
            **kwargs,
        }
        if country is not None:
            params["country"] = country
        if match_exactly is not None:
            params["match_exactly"] = match_exactly
        if get_author_stats is not None:
            params["get_author_stats"] = get_author_stats

        return self.requester.get("/tt/keyword/posts", params=params)

    def full_keyword_search(
        self,
        *,
        keyword: str,
        period: Literal["0", "1", "7", "30", "90", "180"],
        sorting: Literal["0", "1"] | None = None,
        country: str | None = None,
        match_exactly: bool | None = None,
        get_author_stats: bool | None = None,
        **kwargs,
    ):
        params = {
            "keyword": keyword,
            "period": period,
            **kwargs,
        }
        if sorting is not None:
            params["sorting"] = sorting
        if country is not None:
            params["country"] = country
        if match_exactly is not None:
            params["match_exactly"] = match_exactly
        if get_author_stats is not None:
            params["get_author_stats"] = get_author_stats

        return self.requester.get("/tt/keyword/posts", params=params)

    def user_posts_from_username(
        self,
        *,
        username: str,
        depth: int,
        start_cursor: int | None = None,
        oldest_createtime: int | None = None,
        alternative_method: bool | None = None,
        **kwargs,
    ):
        params = {
            "username": username,
            "depth": depth,
            **kwargs,
        }
        if start_cursor is not None:
            params["start_cursor"] = start_cursor
        if oldest_createtime is not None:
            params["oldest_createtime"] = oldest_createtime
        if alternative_method is not None:
            params["alternative_method"] = alternative_method

        return self.requester.get("/tt/user/posts", params=params)

    def user_posts_from_secuid(
        self,
        *,
        sec_uid: str,
        depth: int,
        start_cursor: int | None = None,
        oldest_createtime: int | None = None,
        alternative_method: bool | None = None,
        **kwargs,
    ):
        params = {
            "secUid": sec_uid,
            "depth": depth,
            **kwargs,
        }
        if start_cursor is not None:
            params["start_cursor"] = start_cursor
        if oldest_createtime is not None:
            params["oldest_createtime"] = oldest_createtime
        if alternative_method is not None:
            params["alternative_method"] = alternative_method

        return self.requester.get("/tt/user/posts-from-secuid", params=params)

    def user_info_from_username(self, *, username: str, **kwargs):
        params = {
            "username": username,
            **kwargs,
        }
        return self.requester.get("/tt/user/info-from-secuid", params=params)

    def user_info_from_secuid(
        self,
        *,
        sec_uid: str,
        alternative_method: bool | None = None,
        **kwargs,
    ):
        params = {
            "secUid": sec_uid,
            **kwargs,
        }
        if alternative_method is not None:
            params["alternative_method"] = alternative_method

        return self.requester.get("/tt/user/info-from-secuid", params=params)

    def user_search(self, *, keyword: str, cursor: int, **kwargs):
        params = {
            "keyword": keyword,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/tt/user/search", params=params)

    def post_info(self, *, url: str, **kwargs):
        # TODO: allow awemeid as param?
        params = {
            "url": url,
            **kwargs,
        }
        return self.requester.get("/tt/post/info", params=params)

    def multi_post_info(self, *, post_ids: Sequence[str], **kwargs):
        params = {
            "ids": ",".join(post_ids),
            **kwargs,
        }
        return self.requester.get("/tt/post/multi-info", params=params)

    def post_comments(self, *, aweme_id: str, cursor: int, **kwargs):
        params = {
            "aweme_id": aweme_id,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/tt/post/comments", params=params)

    def post_comment_replies(
        self,
        *,
        aweme_id: str,
        comment_id: str,
        cursor: int,
        **kwargs,
    ):
        params = {
            "aweme_id": aweme_id,
            "comment_id": comment_id,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/tt/post/comment-replies", params=params)

    def music_search(
        self,
        *,
        name: str,
        cursor: int,
        sorting: Literal["0", "1", "2", "3", "4"],
        filter_by: Literal["0", "1", "2"],
        **kwargs,
    ):
        params = {
            "name": name,
            "cursor": cursor,
            "sorting": sorting,
            "filter_by": filter_by,
            **kwargs,
        }
        return self.requester.get("/tt/music/info", params=params)

    def music_posts(self, *, music_id: str, cursor: int, **kwargs):
        params = {
            "music_id": music_id,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/tt/music/posts", params=params)

    def music_details(self, *, music_id: str, **kwargs):
        params = {
            "id": music_id,
            **kwargs,
        }
        return self.requester.get("/tt/music/details", params=params)

    def user_followers(
        self,
        *,
        user_id: str,
        sec_uid: str,
        cursor: int,
        **kwargs,
    ):
        params = {
            "id": user_id,
            "secUid": sec_uid,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/tt/user/followers", params=params)

    def user_followings(
        self,
        *,
        user_id: str,
        sec_uid: str,
        cursor: int,
        page_token: str,
        **kwargs,
    ):
        params = {
            "id": user_id,
            "secUid": sec_uid,
            "cursor": cursor,
            "pageToken": page_token,
            **kwargs,
        }
        return self.requester.get("/tt/user/followings", params=params)

    def user_liked_posts(self, *, sec_uid: str, cursor: int, **kwargs):
        params = {
            "secUid": sec_uid,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/tt/user/liked-posts", params=params)


class EDReddit:
    def __init__(self, requester: Requester):
        self.requester = requester

    def subreddit_posts(
        self,
        *name: str,
        sort: Literal["hot", "new", "top", "rising"],
        period: Literal["hour", "day", "week", "month", "year", "all"],
        cursor: str,
        **kwargs,
    ):
        params = {
            "name": name,
            "sort": sort,
            "period": period,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/reddit/subreddit/posts", params=params)

    def post_comments(self, *, id: str, cursor: str, **kwargs):
        params = {
            "id": id,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/reddit/post/comments", params=params)


class EDTwitch:
    def __init__(self, requester: Requester):
        self.requester = requester

    def keyword_search(
        self,
        *,
        keyword: str,
        type: Literal["videos", "channels", "games"],
        **kwargs,
    ):
        params = {
            "keyword": keyword,
            "type": type,
            **kwargs,
        }
        return self.requester.get("/twitch/search", params=params)

    def user_followers(self, *, username: str, **kwargs):
        params = {
            "username": username,
            **kwargs,
        }
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
        start_cursor: str | None = None,
        alternative_method: bool | None = None,
        **kwargs,
    ):
        params = {
            "user_id": user_id,
            "depth": depth,
            **kwargs,
        }
        if oldest_timestamp is not None:
            params["oldestTimestamp"] = oldest_timestamp
        if chunk_size is not None:
            params["chunkSize"] = chunk_size
        if start_cursor is not None:
            params["startCursor"] = start_cursor
        if alternative_method is not None:
            params["alternativeMethod"] = alternative_method

        return self.requester.get("/instagram/user/posts", params=params)

    def user_basic_stats(self, *, user_id: int, **kwargs):
        params = {
            "user_id": user_id,
            **kwargs,
        }
        return self.requester.get("/instagram/user/basic-info", params=params)

    def user_info(self, *, username: str, **kwargs):
        params = {
            "username": username,
            **kwargs,
        }
        return self.requester.get("/instagram/user/info", params=params)

    def user_detailed_info(self, *, username: str, **kwargs):
        params = {
            "username": username,
            **kwargs,
        }
        return self.requester.get("/instagram/user/detailed-info", params=params)

    def user_followers(self, *, user_id: int, cursor: int, **kwargs):
        params = {
            "user_id": user_id,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/instagram/user/followers", params=params)

    def user_reels(
        self,
        *,
        user_id: int,
        depth: int,
        include_feed_video: bool | None = None,
        oldest_timestamp: int | None = None,
        start_cursor: str | None = None,
        chunk_size: int | None = None,
        **kwargs,
    ):
        params = {
            "user_id": user_id,
            "depth": depth,
            **kwargs,
        }
        if include_feed_video is not None:
            params["includeFeedVideo"] = include_feed_video
        if oldest_timestamp is not None:
            params["oldestTimestamp"] = oldest_timestamp
        if start_cursor is not None:
            params["startCursor"] = start_cursor
        if chunk_size is not None:
            params["chunkSize"] = chunk_size

        return self.requester.get("/instagram/user/reels", params=params)

    def user_tagged_posts(
        self,
        *,
        user_id: int,
        cursor: str | None = None,
        chunk_size: int | None = None,
        **kwargs,
    ):
        params = {
            "user_id": user_id,
            **kwargs,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if chunk_size is not None:
            params["chunkSize"] = chunk_size

        return self.requester.get("/instagram/user/tagged-posts", params=params)

    def post_info_and_comments(
        self,
        *,
        code: str,
        num_comments: int | None = None,
        **kwargs,
    ):
        params = {
            "code": code,
            **kwargs,
        }
        if num_comments is not None:
            params["n_comments_to_fetch"] = num_comments

        return self.requester.get("/instagram/post/details", params=params)

    def hashtag_posts(
        self,
        *,
        hashtag: str,
        cursor: str | None = None,
        chunk_size: int | None = None,
        get_author_info: bool | None = None,
        alternative_method: bool | None = None,
        **kwargs,
    ):
        params = {
            "hashtag": hashtag,
            **kwargs,
        }
        if cursor is not None:
            params["cursor"] = cursor
        if chunk_size is not None:
            params["chunkSize"] = chunk_size
        if get_author_info is not None:
            params["getAuthorInfo"] = get_author_info
        if alternative_method is not None:
            params["alternativeMethod"] = alternative_method

        return self.requester.get("/instagram/hashtag/posts", params=params)

    def music_posts(self, *, music_id: str, cursor: str | None = None, **kwargs):
        params = {
            "music_id": music_id,
            **kwargs,
        }
        if cursor is not None:
            params["cursor"] = cursor
        return self.requester.get("/instagram/music/posts", params=params)

    def search(self, *, text: str, **kwargs):
        params = {
            "text": text,
            **kwargs,
        }
        return self.requester.get("/instagram/search", params=params)


class EDYoutube:
    def __init__(self, requester: Requester):
        self.requester = requester

    def keyword_search(
        self,
        *,
        keyword: str,
        depth: int,
        start_cursor: str | None = None,
        period: Literal["overall", "hour", "today", "week", "month", "year"] | None = None,
        sorting: Literal["relevance", "time", "views", "rating"] | None = None,
        get_additional_info: bool | None = None,
        **kwargs,
    ):
        params = {
            "name": keyword,
            "depth": depth,
            **kwargs,
        }
        if start_cursor is not None:
            params["start_cursor"] = start_cursor
        if period is not None:
            params["period"] = period
        if sorting is not None:
            params["sorting"] = sorting
        if get_additional_info is not None:
            params["get_additional_info"] = get_additional_info

        return self.requester.get("/youtube/search", params=params)

    def featured_category_search(self, *, keyword: str, **kwargs):
        params = {
            "name": keyword,
            **kwargs,
        }
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
        **kwargs,
    ):
        params = {
            "name": hashtag,
            "depth": depth,
            **kwargs,
        }
        if only_shorts is not None:
            params["only_shorts"] = only_shorts

        return self.requester.get("/youtube/hashtag/search", params=params)

    def channel_detailed_info(self, *, channel_id: str, **kwargs):
        params = {
            "browseId": channel_id,
            **kwargs,
        }
        return self.requester.get("/youtube/channel/detailed-info", params=params)

    def channel_videos(self, *, channel_id: str, depth: int, **kwargs):
        params = {
            "browseId": channel_id,
            "depth": depth,
            **kwargs,
        }
        return self.requester.get("/youtube/channel/videos", params=params)

    def channel_shorts(self, *, channel_id: str, depth: int, **kwargs):
        params = {
            "browseId": channel_id,
            "depth": depth,
            **kwargs,
        }
        return self.requester.get("/youtube/channel/shorts", params=params)

    def video_or_short_details(
        self,
        *,
        id: str,
        alternative_method: bool | None = None,
        get_subscribers_count: bool | None = None,
        **kwargs,
    ):
        params = {
            "id": id,
            **kwargs,
        }
        if alternative_method is not None:
            params["alternative_method"] = alternative_method
        if get_subscribers_count is not None:
            params["get_subscribers_count"] = get_subscribers_count

        return self.requester.get(
            "/youtube/channel/get-short-stats",
            params=params,
        )

    def channel_followers(self, *, channel_id: str, **kwargs):
        params = {
            "browseId": channel_id,
            **kwargs,
        }
        return self.requester.get("/youtube/channel/followers", params=params)

    def channel_username_to_id(self, *, name: str, **kwargs):
        params = {
            "name": name,
            **kwargs,
        }
        return self.requester.get("/youtube/channel/name-to-id", params=params)

    def channel_id_to_username(self, *, channel_id: str, **kwargs):
        params = {
            "browserId": channel_id,
            **kwargs,
        }
        return self.requester.get("/youtube/channel/id-to-name", params=params)

    def music_id_to_shorts(
        self,
        *,
        music_id: str,
        depth: int | None = None,
        **kwargs,
    ):
        params = {
            "id": music_id,
            **kwargs,
        }
        if depth is not None:
            params["depth"] = depth

        return self.requester.get("/youtube/music/id-to-shorts", params=params)

    def video_comments(self, *, id: str, cursor: str, **kwargs):
        params = {
            "id": id,
            "cursor": cursor,
            **kwargs,
        }
        return self.requester.get("/youtube/video/comments", params=params)


class EDClient:
    def __init__(self, token: str):
        self.requester = Requester(token)
        self.customer = EDCustomer(self.requester)
        self.tiktok = EDTikTok(self.requester)
        self.instagram = EDInstagram(self.requester)
        self.youtube = EDYoutube(self.requester)
        self.reddit = EDReddit(self.requester)
        self.twitch = EDTwitch(self.requester)

    def request(self, uri: str, **kwargs):
        return self.requester.get(uri, params=kwargs)
