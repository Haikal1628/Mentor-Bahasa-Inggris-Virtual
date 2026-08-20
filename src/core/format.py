import telegramify_markdown
# library untuk mengubah markdown standard menjadi Telegram MarkdownV2 yang valid


def to_telegram_markdown(text: str) -> str:
    """Ubah markdown standard (output dari LLM) menjadi Telegram MarkdownV2 yang valid."""
    return telegramify_markdown.markdownify(text)


# Apa yang dilakukan oleh function telegramify_markdown.markdownify(text)