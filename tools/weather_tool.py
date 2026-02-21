"""Weather tool using OpenWeatherMap API"""
import httpx
from mcp.types import Tool, TextContent
from config import Settings

class WeatherTool:
    def __init__(self, settings: Settings):
        self.api_key = settings.openweather_api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    @staticmethod
    def schema() -> Tool:
        return Tool(name="get_weather", description="Get current weather for a city",
            inputSchema={"type":"object","properties":{"city":{"type":"string"},"units":{"type":"string","enum":["metric","imperial"],"default":"metric"}},"required":["city"]})

    async def run(self, city: str, units: str = "metric") -> list[TextContent]:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self.base_url}/weather",
                params={"q":city,"appid":self.api_key,"units":units})
            r.raise_for_status()
            data = r.json()
            return [TextContent(type="text", text=f"Weather in {city}: {data['weather'][0]['description']}, {data['main']['temp']}°{'C' if units=='metric' else 'F'}, humidity {data['main']['humidity']}%")]