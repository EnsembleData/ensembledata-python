from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Mapping, Sequence

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

from ._requester import Requester

if TYPE_CHECKING:
    from ._response import EDResponse


class UseDefault:
    pass


USE_DEFAULT = UseDefault()


class CustomerEndpoints:
    def __init__(self, requester: Requester):
        self.requester = requester

    def get_usage(
        self,
        *,
        date: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "date": date,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/customer/get-used-units", params=params)

    def get_usage_history(
        self,
        *,
        days: int,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "days": days,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/customer/get-history", params=params)


class TiktokEndpoints:
    def __init__(self, requester: Requester):
        self.requester = requester

    def hashtag_search(
        self,
        *,
        hashtag: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": hashtag,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/hashtag/posts", params=params)

    def full_hashtag_search(
        self,
        *,
        hashtag: str,
        days: int,
        remap_output: bool | UseDefault = USE_DEFAULT,
        max_cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": hashtag,
            "days": days,
            "remap_output": remap_output,
            "max_cursor": max_cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/hashtag/recent-posts", params=params)

    def keyword_search(
        self,
        *,
        keyword: str,
        cursor: int | UseDefault = USE_DEFAULT,
        period: Literal["0", "1", "7", "30", "90", "180"],
        sorting: Literal["0", "1"],
        country: str | UseDefault = USE_DEFAULT,
        match_exactly: bool | UseDefault = USE_DEFAULT,
        get_author_stats: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": keyword,
            "cursor": cursor,
            "period": period,
            "sorting": sorting,
            "country": country,
            "match_exactly": match_exactly,
            "get_author_stats": get_author_stats,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/keyword/search", params=params)

    def full_keyword_search(
        self,
        *,
        keyword: str,
        period: Literal["0", "1", "7", "30", "90", "180"],
        sorting: Literal["0", "1"] | UseDefault = USE_DEFAULT,
        country: str | UseDefault = USE_DEFAULT,
        match_exactly: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": keyword,
            "period": period,
            "sorting": sorting,
            "country": country,
            "match_exactly": match_exactly,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/keyword/full-search", params=params)

    def user_posts_from_username(
        self,
        *,
        username: str,
        depth: int,
        cursor: int | UseDefault = USE_DEFAULT,
        oldest_createtime: int | UseDefault = USE_DEFAULT,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
            "depth": depth,
            "start_cursor": cursor,
            "oldest_createtime": oldest_createtime,
            "alternative_method": alternative_method,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/user/posts", params=params, return_top_level_data=True)

    def user_posts_from_secuid(
        self,
        *,
        sec_uid: str,
        depth: int,
        cursor: int | UseDefault = USE_DEFAULT,
        oldest_createtime: int | UseDefault = USE_DEFAULT,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "secUid": sec_uid,
            "depth": depth,
            "start_cursor": cursor,
            "oldest_createtime": oldest_createtime,
            "alternative_method": alternative_method,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get(
            "/tt/user/posts-from-secuid", params=params, return_top_level_data=True
        )

    def user_info_from_username(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/user/info", params=params)

    def user_info_from_secuid(
        self,
        *,
        sec_uid: str,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "secUid": sec_uid,
            "alternative_method": alternative_method,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/user/info-from-secuid", params=params)

    def user_search(
        self,
        *,
        keyword: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "keyword": keyword,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/user/search", params=params)

    def post_info(
        self,
        *,
        url: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "url": url,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/post/info", params=params)

    def multi_post_info(
        self,
        *,
        aweme_ids: Sequence[str],
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "ids": ";".join(aweme_ids),
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/post/multi-info", params=params)

    def post_comments(
        self,
        *,
        aweme_id: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "aweme_id": aweme_id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/post/comments", params=params)

    def post_comment_replies(
        self,
        *,
        aweme_id: str,
        comment_id: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "aweme_id": aweme_id,
            "comment_id": comment_id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/post/comments-replies", params=params)

    def music_search(
        self,
        *,
        keyword: str,
        cursor: int | UseDefault = USE_DEFAULT,
        sorting: Literal["0", "1", "2", "3", "4"],
        filter_by: Literal["0", "1", "2"],
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": keyword,
            "cursor": cursor,
            "sorting": sorting,
            "filter_by": filter_by,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/music/info", params=params)

    def music_posts(
        self,
        *,
        music_id: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "music_id": music_id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/music/posts", params=params)

    def music_details(
        self,
        *,
        music_id: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": music_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/music/details", params=params)

    def user_followers(
        self,
        *,
        id: str,
        sec_uid: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "secUid": sec_uid,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/user/followers", params=params)

    def user_followings(
        self,
        *,
        id: str,
        sec_uid: str,
        cursor: int | UseDefault = USE_DEFAULT,
        page_token: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "secUid": sec_uid,
            "cursor": cursor,
            "page_token": page_token,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/user/followings", params=params)

    def user_liked_posts(
        self,
        *,
        sec_uid: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "secUid": sec_uid,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/tt/user/liked-posts", params=params)


class YoutubeEndpoints:
    def __init__(self, requester: Requester):
        self.requester = requester

    def keyword_search(
        self,
        *,
        keyword: str,
        depth: int,
        cursor: str | UseDefault = USE_DEFAULT,
        period: Literal["overall", "hour", "today", "week", "month", "year"]
        | UseDefault = USE_DEFAULT,
        sorting: Literal["relevance", "time", "views", "rating"] | UseDefault = USE_DEFAULT,
        get_additional_info: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "keyword": keyword,
            "depth": depth,
            "start_cursor": cursor,
            "period": period,
            "sorting": sorting,
            "get_additional_info": get_additional_info,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/search", params=params)

    def featured_categories_search(
        self,
        *,
        keyword: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": keyword,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/search/featured-categories", params=params)

    def hashtag_search(
        self,
        *,
        hashtag: str,
        depth: int,
        only_shorts: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": hashtag,
            "depth": depth,
            "only_shorts": only_shorts,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/hashtag/search", params=params)

    def channel_detailed_info(
        self,
        *,
        channel_id: str,
        from_url: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
            "from_url": from_url,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/channel/detailed-info", params=params)

    def channel_videos(
        self,
        *,
        channel_id: str,
        depth: int,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
            "depth": depth,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/channel/videos", params=params)

    def channel_shorts(
        self,
        *,
        channel_id: str,
        depth: int,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
            "depth": depth,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/channel/shorts", params=params)

    def video_details(
        self,
        *,
        id: str,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        get_subscribers_count: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "alternative_method": alternative_method,
            "get_subscribers_count": get_subscribers_count,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/channel/get-short-stats", params=params)

    def channel_subscribers(
        self,
        *,
        channel_id: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/channel/followers", params=params)

    def channel_username_to_id(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/channel/name-to-id", params=params)

    def channel_id_to_username(
        self,
        *,
        channel_id: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/channel/id-to-name", params=params)

    def music_id_to_shorts(
        self,
        *,
        music_id: str,
        depth: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": music_id,
            "depth": depth,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/music/id-to-shorts", params=params)

    def video_comments(
        self,
        *,
        id: str,
        cursor: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/youtube/video/comments", params=params)


class InstagramEndpoints:
    def __init__(self, requester: Requester):
        self.requester = requester

    def user_posts(
        self,
        *,
        user_id: int,
        depth: int,
        oldest_timestamp: int | UseDefault = USE_DEFAULT,
        chunk_size: int | UseDefault = USE_DEFAULT,
        cursor: str | UseDefault = USE_DEFAULT,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
            "depth": depth,
            "oldest_timestamp": oldest_timestamp,
            "chunk_size": chunk_size,
            "start_cursor": cursor,
            "alternative_method": alternative_method,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/user/posts", params=params)

    def user_basic_stats(
        self,
        *,
        user_id: int,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/user/basic-info", params=params)

    def user_info(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/user/info", params=params)

    def user_detailed_info(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/user/detailed-info", params=params)

    def user_followers(
        self,
        *,
        user_id: int,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/user/followers", params=params)

    def user_reels(
        self,
        *,
        user_id: int,
        depth: int,
        include_feed_video: bool | UseDefault = USE_DEFAULT,
        oldest_timestamp: int | UseDefault = USE_DEFAULT,
        cursor: str | UseDefault = USE_DEFAULT,
        chunk_size: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
            "depth": depth,
            "include_feed_video": include_feed_video,
            "oldest_timestamp": oldest_timestamp,
            "start_cursor": cursor,
            "chunk_size": chunk_size,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/user/reels", params=params)

    def user_tagged_posts(
        self,
        *,
        user_id: int,
        cursor: str | UseDefault = USE_DEFAULT,
        chunk_size: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
            "cursor": cursor,
            "chunk_size": chunk_size,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/user/tagged-posts", params=params)

    def post_info_and_comments(
        self,
        *,
        code: str,
        num_comments: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "code": code,
            "n_comments_to_fetch": num_comments,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/post/details", params=params)

    def hashtag_posts(
        self,
        *,
        hashtag: str,
        cursor: str | UseDefault = USE_DEFAULT,
        chunk_size: int | UseDefault = USE_DEFAULT,
        get_author_info: bool | UseDefault = USE_DEFAULT,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": hashtag,
            "cursor": cursor,
            "chunk_size": chunk_size,
            "get_author_info": get_author_info,
            "alternative_method": alternative_method,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/hashtag/posts", params=params)

    def music_posts(
        self,
        *,
        music_id: str,
        cursor: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": music_id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/music/posts", params=params)

    def search(
        self,
        *,
        text: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "text": text,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/instagram/search", params=params)


class TwitchEndpoints:
    def __init__(self, requester: Requester):
        self.requester = requester

    def keyword_search(
        self,
        *,
        keyword: str,
        depth: int,
        type: Literal["videos", "channels", "games"],
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "keyword": keyword,
            "depth": depth,
            "type": type,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/twitch/search", params=params)

    def user_followers(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/twitch/user/followers", params=params)


class RedditEndpoints:
    def __init__(self, requester: Requester):
        self.requester = requester

    def subreddit_posts(
        self,
        *,
        name: str,
        sort: Literal["hot", "new", "top", "rising"],
        period: Literal["hour", "day", "week", "month", "year", "all"],
        cursor: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": name,
            "sort": sort,
            "period": period,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/reddit/subreddit/posts", params=params)

    def post_comments(
        self,
        *,
        id: str,
        cursor: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return self.requester.get("/reddit/post/comments", params=params)


class EDClient:
    def __init__(self, token: str, *, timeout: int = 600, max_network_retries: int = 3):
        self.requester = Requester(token, timeout=timeout, max_network_retries=max_network_retries)
        self.customer = CustomerEndpoints(self.requester)
        self.tiktok = TiktokEndpoints(self.requester)
        self.youtube = YoutubeEndpoints(self.requester)
        self.instagram = InstagramEndpoints(self.requester)
        self.twitch = TwitchEndpoints(self.requester)
        self.reddit = RedditEndpoints(self.requester)

    async def request(self, uri: str, params: Mapping[str, Any] | None = None) -> EDResponse:
        return self.requester.get(uri, params=params or {})
