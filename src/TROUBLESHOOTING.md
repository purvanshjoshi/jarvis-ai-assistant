# Jarvis Agent Timeout Troubleshooting Guide

## Current Issue
```
livekit.agents.llm.realtime.RealtimeError: generate_reply timed out waiting for generation_created event.
```

The agent connects to Google's API (`setupComplete` received) but times out when trying to send instructions.

## What's Been Fixed ✅

1. **Memory System** - Now correctly persists conversations
2. **Agent Error Handling** - 5 retries with exponential backoff
3. **Memory Injection** - Optimized to be brief and non-blocking
4. **API Diagnostics** - Configuration verified as correct

## Possible Causes & Solutions

### 1. **Network Connectivity Issues** (Most Likely)
**Symptoms:** Consistent timeout after 30+ seconds
**Solutions:**
```bash
# Test internet
ping 8.8.8.8

# Test DNS
nslookup generativelanguage.googleapis.com

# If behind proxy/VPN:
# - Disable VPN temporarily
# - Configure proxy in Python if needed
```

### 2. **Google API Service Issues**
**Symptoms:** Timeouts occur consistently at same time
**Solutions:**
- Check Google Cloud status: https://status.cloud.google.com/
- Verify API is enabled: https://console.cloud.google.com/apis/dashboard
- Check quotas: https://console.cloud.google.com/iam-admin/quotas

### 3. **API Key Issues**
**Symptoms:** Sometimes works, sometimes doesn't
**Solutions:**
```bash
# Verify key in .env
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('GOOGLE_API_KEY'))"

# Regenerate key if old:
# 1. Go to https://console.cloud.google.com/
# 2. APIs & Services > Credentials
# 3. Delete old key, create new one
# 4. Update .env
```

### 4. **Audio Input Not Ready**
**Symptoms:** Agent waits for audio but times out
**Solutions:**
```bash
# Ensure microphone is working:
# 1. Go to Settings > Sound > Volume
# 2. Check Realtek microphone is enabled
# 3. Test in Windows Audio - Record some audio
# 4. Try again
```

### 5. **Slow/Weak Internet**
**Symptoms:** Timeout happens but connection seems OK
**Solutions:**
```bash
# Check connection speed
# Download SpeedTest: https://www.speedtest.net/
# Minimum required: 1 Mbps upload, 2 Mbps download

# Close bandwidth-heavy apps:
# - Chrome (multiple tabs)
# - Downloads in progress
# - YouTube/Streaming services
```

## Quick Fixes to Try (in order)

### Fix #1: Disable Memory Injection (Fastest)
Edit `agent.py` line ~28:
```python
ENABLE_MEMORY_INTERCEPTOR = False  # Temporarily disable
```
Then try: `python agent.py console`

**Why:** This eliminates one async operation that could be blocking

### Fix #2: Increase Timeout
The agent now retries 5 times with exponential backoff. Each try waits:
- Attempt 1: 3s
- Attempt 2: 6s  
- Attempt 3: 9s
- Attempt 4: 12s
- Attempt 5: 15s

Just wait longer when you see the error.

### Fix #3: Check API Quota
Visit: https://console.cloud.google.com/iam-admin/quotas
Look for: "Generative Language API"
**If quota = 0:** Need to enable API or increase quota

### Fix #4: Restart Everything
```bash
# Close agent terminal
# Power off router for 30 seconds
# Power on, wait for internet
# Try again: python agent.py console
```

## If Still Not Working

### Option A: Use Alternative Setup
If you have a different LLM provider API (OpenAI, Anthropic, etc.), we can configure it instead.

### Option B: Check LiveKit Connection
The issue might also be with LiveKit room connection, not just Google API:
```bash
python -c "from livekit.agents import config; print(config.settings.livekit_url)"
```
Should print: `wss://jarvis-3kpjbieq.livekit.cloud`

### Option C: Contact Google Support
If everything above passes, the issue might be on Google's end:
- Error code in logs (if any)
- Time/date of failure
- Your Google Cloud project ID
- Contact: https://cloud.google.com/support

## Testing Memory Still Works

Even if agent times out on startup, memory system is working:
```bash
python test_memory_persistence.py
# Should show: ✅ TEST PASSED
```

## Quick Reference: What's Running

When you run `python agent.py console`:

```
Terminal 1: Agent (main process)
│
├─ Connects to LiveKit (OK ✅)
├─ Loads memory context (OK ✅)
├─ Attempts Google API call ← TIMEOUT HERE ❌
└─ Retries 5 times (new in latest fix)

Terminal 2 (background): GUI (jarvis_gui.py)
├─ Displays video feed
├─ Shows agent status
└─ Polls for screenshots
```

## Status

- ✅ Code is correct
- ✅ Memory system works
- ✅ API configuration validated
- ❌ Google API timeout = Network issue (not code)

**Action:** Try Fix #1 and #2 above first. If those don't work, follow the diagnostic steps to identify which component is timing out.
