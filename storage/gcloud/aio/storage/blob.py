from typing import Any

import aiohttp


class Blob:
    def __init__(self, bucket, name, metadata):
        self.__dict__.update(**metadata)

        self.bucket = bucket
        self.name = name
        self.size = int(self.size)

    @property
    def chunk_size(self) -> int:
        return self.size + (262144 - (self.size % 262144))

    async def download(self, session = None):
        return await self.bucket.storage.download(self.bucket.name, self.name,
                                                  session=session)

    async def upload(self, data,
                     session = None):
        metadata = await self.bucket.storage.upload(
            self.bucket.name, self.name, data, session=session)

        self.__dict__.update(metadata)
        return metadata
