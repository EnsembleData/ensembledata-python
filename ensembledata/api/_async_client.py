from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Mapping, Sequence

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

from ._requester import AsyncRequester

if TYPE_CHECKING:
    from ._response import EDResponse


class UseDefault:
    pass


USE_DEFAULT = UseDefault()


class CustomerEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def get_usage(
        self,
        *,
        date: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "date": date,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/customer/get-used-units", params=params, timeout=timeout)

    async def get_usage_history(
        self,
        *,
        days: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "days": days,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/customer/get-history", params=params, timeout=timeout)


class TiktokEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def hashtag_search(
        self,
        *,
        hashtag: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": hashtag,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/hashtag/posts", params=params, timeout=timeout)

    async def full_hashtag_search(
        self,
        *,
        hashtag: str,
        days: int,
        remap_output: bool | UseDefault = USE_DEFAULT,
        max_cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get("/tt/hashtag/recent-posts", params=params, timeout=timeout)

    async def keyword_search(
        self,
        *,
        keyword: str,
        cursor: int | UseDefault = USE_DEFAULT,
        period: Literal["0", "1", "7", "30", "90", "180"],
        sorting: Literal["0", "1"] | UseDefault = USE_DEFAULT,
        country: str | UseDefault = USE_DEFAULT,
        match_exactly: bool | UseDefault = USE_DEFAULT,
        get_author_stats: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get("/tt/keyword/search", params=params, timeout=timeout)

    async def full_keyword_search(
        self,
        *,
        keyword: str,
        period: Literal["0", "1", "7", "30", "90", "180"],
        sorting: Literal["0", "1"] | UseDefault = USE_DEFAULT,
        country: str | UseDefault = USE_DEFAULT,
        match_exactly: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get("/tt/keyword/full-search", params=params, timeout=timeout)

    async def user_posts_from_username(
        self,
        *,
        username: str,
        depth: int,
        cursor: int | UseDefault = USE_DEFAULT,
        oldest_createtime: int | UseDefault = USE_DEFAULT,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get(
            "/tt/user/posts", params=params, timeout=timeout, return_top_level_data=True
        )

    async def user_posts_from_secuid(
        self,
        *,
        sec_uid: str,
        depth: int,
        cursor: int | UseDefault = USE_DEFAULT,
        oldest_createtime: int | UseDefault = USE_DEFAULT,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get(
            "/tt/user/posts-from-secuid", params=params, timeout=timeout, return_top_level_data=True
        )

    async def user_info_from_username(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/user/info", params=params, timeout=timeout)

    async def user_info_from_secuid(
        self,
        *,
        sec_uid: str,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "secUid": sec_uid,
            "alternative_method": alternative_method,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/user/info-from-secuid", params=params, timeout=timeout)

    async def user_search(
        self,
        *,
        keyword: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "keyword": keyword,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/user/search", params=params, timeout=timeout)

    async def post_info(
        self,
        *,
        url: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "url": url,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/post/info", params=params, timeout=timeout)

    async def multi_post_info(
        self,
        *,
        aweme_ids: Sequence[str],
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "ids": ";".join(aweme_ids),
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/post/multi-info", params=params, timeout=timeout)

    async def post_comments(
        self,
        *,
        aweme_id: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "aweme_id": aweme_id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/post/comments", params=params, timeout=timeout)

    async def post_comment_replies(
        self,
        *,
        aweme_id: str,
        comment_id: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "aweme_id": aweme_id,
            "comment_id": comment_id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/post/comments-replies", params=params, timeout=timeout)

    async def music_search(
        self,
        *,
        keyword: str,
        cursor: int | UseDefault = USE_DEFAULT,
        sorting: Literal["0", "1", "2", "3", "4"] | UseDefault = USE_DEFAULT,
        filter_by: Literal["0", "1", "2"] | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get("/tt/music/info", params=params, timeout=timeout)

    async def music_posts(
        self,
        *,
        music_id: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "music_id": music_id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/music/posts", params=params, timeout=timeout)

    async def music_details(
        self,
        *,
        music_id: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": music_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/music/details", params=params, timeout=timeout)

    async def user_followers(
        self,
        *,
        id: str,
        sec_uid: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "secUid": sec_uid,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/user/followers", params=params, timeout=timeout)

    async def user_followings(
        self,
        *,
        id: str,
        sec_uid: str,
        cursor: int | UseDefault = USE_DEFAULT,
        page_token: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get("/tt/user/followings", params=params, timeout=timeout)

    async def user_liked_posts(
        self,
        *,
        sec_uid: str,
        cursor: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "secUid": sec_uid,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/user/liked-posts", params=params, timeout=timeout)

    async def lives_search(
        self,
        *,
        keyword: str,
        cursor: int | UseDefault = USE_DEFAULT,
        country: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "keyword": keyword,
            "cursor": cursor,
            "country": country,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/tt/live/search", params=params, timeout=timeout)


class YoutubeEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def keyword_search(
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
        timeout: float | None = None,
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
        return await self.requester.get("/youtube/search", params=params, timeout=timeout)

    async def featured_categories_search(
        self,
        *,
        keyword: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": keyword,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/youtube/search/featured-categories", params=params, timeout=timeout
        )

    async def hashtag_search(
        self,
        *,
        hashtag: str,
        depth: int,
        only_shorts: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": hashtag,
            "depth": depth,
            "only_shorts": only_shorts,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/youtube/hashtag/search", params=params, timeout=timeout)

    async def channel_detailed_info(
        self,
        *,
        channel_id: str,
        from_url: bool | UseDefault = USE_DEFAULT,
        get_additional_info: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
            "from_url": from_url,
            "get_additional_info": get_additional_info,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/youtube/channel/detailed-info", params=params, timeout=timeout
        )

    async def channel_videos(
        self,
        *,
        channel_id: str,
        depth: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
            "depth": depth,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/youtube/channel/videos", params=params, timeout=timeout)

    async def channel_shorts(
        self,
        *,
        channel_id: str,
        depth: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
            "depth": depth,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/youtube/channel/shorts", params=params, timeout=timeout)

    async def channel_streams(
        self,
        *,
        channel_id: str,
        depth: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
            "depth": depth,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/youtube/channel/streams", params=params, timeout=timeout)

    async def video_details(
        self,
        *,
        id: str,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        get_subscribers_count: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "alternative_method": alternative_method,
            "get_subscribers_count": get_subscribers_count,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/youtube/channel/get-short-stats", params=params, timeout=timeout
        )

    async def channel_subscribers(
        self,
        *,
        channel_id: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/youtube/channel/followers", params=params, timeout=timeout
        )

    async def channel_username_to_id(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/youtube/channel/name-to-id", params=params, timeout=timeout
        )

    async def channel_id_to_username(
        self,
        *,
        channel_id: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "browseId": channel_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/youtube/channel/id-to-name", params=params, timeout=timeout
        )

    async def music_id_to_shorts(
        self,
        *,
        music_id: str,
        depth: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": music_id,
            "depth": depth,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/youtube/music/id-to-shorts", params=params, timeout=timeout
        )

    async def video_comments(
        self,
        *,
        id: str,
        cursor: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/youtube/video/comments", params=params, timeout=timeout)


class InstagramEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def user_posts(
        self,
        *,
        user_id: int,
        depth: int,
        oldest_timestamp: int | UseDefault = USE_DEFAULT,
        chunk_size: int | UseDefault = USE_DEFAULT,
        cursor: str | UseDefault = USE_DEFAULT,
        alternative_method: bool | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get("/instagram/user/posts", params=params, timeout=timeout)

    async def user_basic_stats(
        self,
        *,
        user_id: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/instagram/user/basic-info", params=params, timeout=timeout
        )

    async def user_info(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/instagram/user/info", params=params, timeout=timeout)

    async def user_detailed_info(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/instagram/user/detailed-info", params=params, timeout=timeout
        )

    async def user_followers(
        self,
        *,
        user_id: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/instagram/user/followers", params=params, timeout=timeout)

    async def user_reels(
        self,
        *,
        user_id: int,
        depth: int,
        include_feed_video: bool | UseDefault = USE_DEFAULT,
        oldest_timestamp: int | UseDefault = USE_DEFAULT,
        cursor: str | UseDefault = USE_DEFAULT,
        chunk_size: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get("/instagram/user/reels", params=params, timeout=timeout)

    async def user_tagged_posts(
        self,
        *,
        user_id: int,
        cursor: str | UseDefault = USE_DEFAULT,
        chunk_size: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "user_id": user_id,
            "cursor": cursor,
            "chunk_size": chunk_size,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get(
            "/instagram/user/tagged-posts", params=params, timeout=timeout
        )

    async def post_info_and_comments(
        self,
        *,
        code: str,
        num_comments: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "code": code,
            "n_comments_to_fetch": num_comments,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/instagram/post/details", params=params, timeout=timeout)

    async def music_posts(
        self,
        *,
        music_id: str,
        cursor: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": music_id,
            "cursor": cursor,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/instagram/music/posts", params=params, timeout=timeout)

    async def search(
        self,
        *,
        text: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "text": text,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/instagram/search", params=params, timeout=timeout)


class TwitchEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def keyword_search(
        self,
        *,
        keyword: str,
        depth: int,
        type: Literal["videos", "channels", "games"],
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "keyword": keyword,
            "depth": depth,
            "type": type,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/twitch/search", params=params, timeout=timeout)

    async def user_followers(
        self,
        *,
        username: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "username": username,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/twitch/user/followers", params=params, timeout=timeout)


class RedditEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def subreddit_posts(
        self,
        *,
        name: str,
        sort: Literal["hot", "new", "top", "rising"],
        period: Literal["hour", "day", "week", "month", "year", "all"],
        cursor: str | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
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
        return await self.requester.get("/reddit/subreddit/posts", params=params, timeout=timeout)

    async def post_comments(
        self,
        *,
        permalink: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "permalink": permalink,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/reddit/post/comments", params=params, timeout=timeout)


class TwitterEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def user_info(
        self,
        *,
        name: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": name,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/twitter/user/info", params=params, timeout=timeout)

    async def user_tweets(
        self,
        *,
        id: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/twitter/user/tweets", params=params, timeout=timeout)

    async def post_info(
        self,
        *,
        id: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/twitter/post/info", params=params, timeout=timeout)


class ThreadsEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def search_keyword(
        self,
        *,
        name: str,
        sorting: Literal["0", "1"] | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": name,
            "sorting": sorting,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/threads/keyword/search", params=params, timeout=timeout)

    async def user_search(
        self,
        *,
        name: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": name,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/threads/user/search", params=params, timeout=timeout)

    async def user_info(
        self,
        *,
        id: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/threads/user/info", params=params, timeout=timeout)

    async def user_posts(
        self,
        *,
        id: int,
        chunk_size: int | UseDefault = USE_DEFAULT,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
            "chunk_size": chunk_size,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/threads/user/posts", params=params, timeout=timeout)

    async def post_replies(
        self,
        *,
        id: int,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "id": id,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/threads/post/replies", params=params, timeout=timeout)


class SnapchatEndpoints:
    def __init__(self, requester: AsyncRequester):
        self.requester = requester

    async def user_info(
        self,
        *,
        name: str,
        extra_params: Mapping[str, Any] | None = None,
        timeout: float | None = None,
    ) -> EDResponse:
        params: dict[str, Any] = {
            "name": name,
        }
        if extra_params is not None:
            params = {**extra_params, **params}
        params = {k: v for k, v in params.items() if not (v is None or v is USE_DEFAULT)}
        return await self.requester.get("/snapchat/user/info", params=params, timeout=timeout)


class EDAsyncClient:
    def __init__(self, token: str, *, timeout: float = 600, max_network_retries: int = 3):
        self.requester = AsyncRequester(
            token, timeout=timeout, max_network_retries=max_network_retries
        )
        self.customer = CustomerEndpoints(self.requester)
        self.tiktok = TiktokEndpoints(self.requester)
        self.youtube = YoutubeEndpoints(self.requester)
        self.instagram = InstagramEndpoints(self.requester)
        self.twitch = TwitchEndpoints(self.requester)
        self.reddit = RedditEndpoints(self.requester)
        self.twitter = TwitterEndpoints(self.requester)
        self.threads = ThreadsEndpoints(self.requester)
        self.snapchat = SnapchatEndpoints(self.requester)

    async def request(self, uri: str, params: Mapping[str, Any] | None = None) -> EDResponse:
        return await self.requester.get(uri, params=params or {})
