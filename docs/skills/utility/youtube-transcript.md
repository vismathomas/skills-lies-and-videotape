---
title: YouTube Transcript Extraction
description: "Extract transcripts from YouTube videos for research and documentation. Uses open-source tools only (yt-dlp, Whisper)."
---

# YouTube Transcript Extraction

> Extract transcripts from YouTube videos for research and documentation. Uses open-source tools only (yt-dlp, Whisper).

:material-tag: `utility` · :material-github: [https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript)

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/youtube-transcript/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/youtube-transcript/SKILL.md){ .md-button .md-button--primary }

---

Extracts transcripts from YouTube videos for research and documentation. Uses a tiered approach: manual subtitles first, then auto-generated, then Whisper transcription as fallback.

## Usage Examples

### Extract a video transcript

```
Extract the transcript from this YouTube conference talk: https://youtube.com/watch?v=example
```

### Research from video

```
Get the transcript from this tutorial video and create a summary of the key points.
```

### Batch extraction

```
Extract transcripts from these 3 YouTube videos for our research project.
```

## Credits

Based on: [https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript)

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # YouTube Transcript Extraction
    
    Extract transcripts from YouTube videos for research, documentation, and learning.
    
    ## When to Use
    
    - Extracting content from tutorial videos for documentation
    - Researching topics covered in conference talks
    - Creating text summaries of video content
    - Building training/reference material from video sources
    - Supporting `research` with video-based sources
    
    ## Prerequisites
    
    ### Required
    
    - **yt-dlp**: YouTube video/subtitle downloader (open-source)
      ```bash
      # Install
      pip install yt-dlp
      # or
      brew install yt-dlp
      # or
      winget install yt-dlp
      ```
    
    ### Optional (for videos without subtitles)
    
    - **Whisper**: OpenAI's open-source speech-to-text model
      ```bash
      pip install openai-whisper
      ```
    
    ## Transcript Extraction — Tiered Approach
    
    Always try the cheapest/fastest method first:
    
    ### Tier 1: Manual Subtitles (Preferred)
    
    Human-written subtitles — highest quality, fastest extraction.
    
    ```bash
    # List available subtitles
    yt-dlp --list-subs "VIDEO_URL"
    
    # Download manual subtitles (English)
    yt-dlp --write-sub --sub-lang en --skip-download -o "transcript" "VIDEO_URL"
    
    # Convert to plain text
    yt-dlp --write-sub --sub-lang en --sub-format vtt --skip-download -o "transcript" "VIDEO_URL"
    ```
    
    **Post-processing**: Strip VTT/SRT timing markers to produce clean text:
    ```python
    import re
    
    def clean_vtt(vtt_content: str) -> str:
        """Remove VTT formatting, timestamps, and duplicates."""
        lines = vtt_content.split('\n')
        clean_lines = []
        seen = set()
        for line in lines:
            # Skip headers, timestamps, positioning
            if line.startswith('WEBVTT') or '-->' in line or line.strip() == '':
                continue
            if re.match(r'^\d+$', line.strip()):
                continue
            # Remove inline tags
            text = re.sub(r'<[^>]+>', '', line).strip()
            if text and text not in seen:
                seen.add(text)
                clean_lines.append(text)
        return ' '.join(clean_lines)
    ```
    
    ### Tier 2: Auto-Generated Subtitles
    
    YouTube's automatic captions — lower quality but widely available.
    
    ```bash
    # Download auto-generated subtitles
    yt-dlp --write-auto-sub --sub-lang en --skip-download -o "transcript" "VIDEO_URL"
    ```
    
    **Note**: Auto-generated subtitles often have:
    - No punctuation
    - Speaker identification issues
    - Technical term errors
    
    Apply additional cleanup:
    ```python
    def improve_auto_transcript(text: str) -> str:
        """Add basic sentence structure to auto-generated transcripts."""
        # Split into rough sentences (every ~15 words or at natural breaks)
        words = text.split()
        sentences = []
        current = []
        for word in words:
            current.append(word)
            if len(current) >= 15 and word.endswith(('.',  '?', '!', ',')):
                sentences.append(' '.join(current))
                current = []
        if current:
            sentences.append(' '.join(current))
        return '\n'.join(sentences)
    ```
    
    ### Tier 3: Whisper Transcription (Fallback)
    
    For videos with no subtitles at all — download audio and transcribe locally.
    
    ```bash
    # Download audio only
    yt-dlp -x --audio-format mp3 -o "audio.%(ext)s" "VIDEO_URL"
    
    # Transcribe with Whisper
    whisper audio.mp3 --model base --output_format txt --language en
    ```
    
    **Whisper model sizes** (trade-off: speed vs accuracy):
    
    | Model | Size | Speed | Accuracy | Use When |
    |-------|------|-------|----------|----------|
    | `tiny` | 39M | Fastest | Lower | Quick rough transcript |
    | `base` | 74M | Fast | Good | Default choice |
    | `small` | 244M | Medium | Better | Important content |
    | `medium` | 769M | Slow | High | Critical accuracy needed |
    | `large` | 1550M | Slowest | Highest | Maximum quality required |
    
    ## Workflow
    
    ### Step 1: Validate URL
    
    ```python
    import re
    
    def is_youtube_url(url: str) -> bool:
        """Check if URL is a valid YouTube link."""
        patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+',
            r'(?:https?://)?youtu\.be/[\w-]+',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/[\w-]+',
        ]
        return any(re.match(p, url) for p in patterns)
    ```
    
    ### Step 2: Get Video Metadata
    
    ```bash
    # Get title, duration, description
    yt-dlp --print title --print duration_string --print description --skip-download "VIDEO_URL"
    ```
    
    ### Step 3: Extract Transcript (Tiered)
    
    ```
    1. Try manual subtitles (--write-sub)
       ├─ Found → Clean VTT/SRT → Done ✅
       └─ Not found → Continue
    2. Try auto-generated subtitles (--write-auto-sub)
       ├─ Found → Clean + improve → Done ✅
       └─ Not found → Continue
    3. Download audio + Whisper transcription
       ├─ Whisper available → Transcribe → Done ✅
       └─ Whisper not available → Report: no transcript possible ❌
    ```
    
    ### Step 4: Output
    
    Save transcript to project docs:
    
    ```markdown
    # Transcript: {Video Title}
    
    - **Source**: {YouTube URL}
    - **Duration**: {duration}
    - **Extracted**: {date}
    - **Method**: {manual-subs | auto-subs | whisper-{model}}
    
    ---
    
    {transcript text}
    ```
    
    ## Integration with research
    
    When invoked by `research`, transcripts feed directly into research findings:
    
    ```markdown
    ## Research: {topic}
    
    ### Video Sources
    - [{Video Title}]({URL}) — {key takeaways from transcript}
    ```
    
    ## Anti-Patterns
    
    - **DON'T** download full video when only transcript is needed
    - **DON'T** use Whisper when subtitles are available (wasteful)
    - **DON'T** skip the tiered approach — always try cheapest first
    - **DON'T** store large audio files in the project — clean up after transcription
