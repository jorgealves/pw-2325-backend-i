from pydantic import BaseModel, Field
from pydantic_core.core_schema import UrlSchema


class ShortUrlRequest(BaseModel):

    source_url: UrlSchema = Field(
        description="The source url"
    )
