import asyncio

# Importing this library breaks the subsequent fork
import toml_rs

from playwright.async_api import async_playwright


async def main() -> None:
    playwright = await async_playwright().start()
    await playwright.stop()


if __name__ == "__main__":
    asyncio.run(main())
