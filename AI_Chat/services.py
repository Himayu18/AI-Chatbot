import os 
import shutil
import logging
from django.conf import settings
from openai import AsyncOpenAI,APIError
from tenacity import retry,stop_after_attempt,wait_exponential



logger = logging.getLogger(__name__)

client = AsyncOpenAI(
    api_key=settings.PERPLEXITY_API_KEY,
    base_url="https://api.perplexity.ai" 
)

class PerplexityService:
    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1,min=2,max=10)
    )
    async def stream_answer(user_message,model="sonar"):
        try:
            stream = await client.chat.completions.create(
                model=model,
                messages=[
                    {
                    "role":"system",
                     "content":"You are a helpful ai assistant"
                     },
                     {
                         "role":"user",
                         "content":user_message
                     }
                ],
                stream=True,
                timeout=30.0
                )
            async for chunk in stream:
                content = chunk.choices[0].delta.content
                if content:
                    yield content
        except APIError as e:
            logger.error(f"perplexity Api Error: {e}")
            raise e            
            