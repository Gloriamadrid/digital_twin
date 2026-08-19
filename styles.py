"""Styling constants for the digital twin Gradio app."""

GOLD = "#ecad8a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
:root {
    --twin-gold: #ecad8a;
    --twin-blue: #209dd7;
    --twin-purple: #753991;
    --twin-bg: #0d0d10;
    --twin-surface: #16161b;
    --twin-surface-2: #1c1c22;
    --twin-border: #2a2a32;
    --twin-border-strong: #3a3a44;
    --twin-text: #ececef;
    --twin-muted: #8c8c95;
}

/* Light mode overrides */
body:not(.dark) {
    --twin-bg: #f4f4f6;
    --twin-surface: #ffffff;
    --twin-surface-2: #ededf0;
    --twin-border: #dcdce2;
    --twin-border-strong: #b8b8c0;
    --twin-text: #1a1a20;
    --twin-muted: #6a6a72;
}

/* Global container styling */
body, .gradio-container {
    background-color: var(--twin-bg) !important;
    color: var(--twin-text) !important;
}

/* Header typography */
h1, h2, h3 {
    color: var(--twin-text) !important;
    font-weight: 700 !important;
}

/* Sharp corners on structural elements */
.chatbot, .block, .form, button, input, textarea, .examples button {
    border-radius: 0 !important;
}

/* Transparent block surfaces */
.block, .form {
    background: transparent !important;
    box-shadow: none !important;
}

/* Hide header label strip */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
    display: none !important;
}

/* Main Chatbot container framing */
.chatbot, .chatbot.block {
    background: var(--twin-surface) !important;
    border: 1px solid var(--twin-border) !important;
    min-height: 460px !important;
    box-shadow: none !important;
}

.chatbot .placeholder, .chatbot .placeholder * {
    color: var(--twin-muted) !important;
}
"""