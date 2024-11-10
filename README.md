# Anti-Scraping Toolkit

A comprehensive guide to understanding and handling web scraping blocks, detection mechanisms, and countermeasures. This repository contains detailed information and source code about various anti-scraping techniques and how to handle them effectively.

## Table of Contents
1. [Server-Side Perspective](#server-side-perspective)
2. [Browser-Side Detection](#browser-side-detection)
3. [Simulating Human Behavior](#simulating-human-behavior)
4. [Headless Mode Considerations](#headless-mode-considerations)
5. [Fingerprinting Techniques](#fingerprinting-techniques)
6. [Cookies and Sessions](#cookies-and-sessions)

## Server-Side Perspective

Understanding HTTP protocol is fundamental when discussing web scraping detection. During client-server communication, several pieces of client information are shared with the server. Let's examine the key components:

### 1. Headers

The most significant header for scraping detection is the **User-Agent**. This header contains crucial information that can contribute to blocking, including:
- Browser type and version
- Operating system and architecture
- Device information
- Rendering engine
- Compatibility data

Example of a typical User-Agent:
```plaintext
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
```

### 2. IP Address

The IP address is transmitted during HTTP communication at the connection establishment phase. Combined with the User-Agent, it forms the basis for basic blocking systems. If multiple requests come from the same IP with identical User-Agents, it's a strong indicator of automated activity.

Note: IP-based detection isn't foolproof as multiple users can share the same IP address (e.g., public networks, NAT).

### Demonstration

Please, refer to the [api_block_userag.py](./examples/api_block_userag.py) for demonstration.

## Browser-Side Detection

Browser-side detection becomes more sophisticated through JavaScript capabilities. Key aspects include:

### Navigator Object

The navigator object provides extensive information about the browser environment. A critical property for scraping detection is navigator.webdriver, which can instantly reveal automated browsers.

Popular sites implementing this detection include:

- Municipal consultation systems
- E-commerce platforms
- Social media sites

### Countermeasures

Libraries like [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) help bypass these detection mechanisms by:

- Modifying webdriver flags
- Implementing stealth patches
- Masking automation signatures

## Simulating Human Behavior

JavaScript can detect automated behavior through various events and patterns:

### Click Detection

- Hover events
- Click positioning
- Timing patterns
- Mouse movement trajectories

### Demonstration

To demonstrate automated click detection:
1. Open [robotic_click.html](./examples/robotic_click.html) in your browser
2. Access the browser's console (F12 or right-click -> Inspect -> Console)
3. Execute the following JavaScript code:

```javascript
var button = document.querySelector("#botao");
button.click()
```
The script will identify this as automated behavior since the hover event (which typically occurs when a real user moves their mouse over the button) is not triggered during this programmatic click execution.


### Solution: ActionChains

Selenium's ActionChains module provides methods to simulate more natural user interactions:

- Natural mouse movements
- Proper event triggering
- Randomized timing
- Hover simulation

You can test this solution running the [bypass_robotic_click.py](./examples/bypass_robotic_click.py) script.

## Headless Mode Considerations

When using headless browsers, consider these crucial factors:

### 1. User-Agent Modification
   - Default headless User-Agents contain revealing strings
   - Always customize User-Agent in headless mode

### 2. Required Flags
   - Enable WebGL: --enable-webgl
   - Enable necessary browser features
   - Maintain browser fingerprint consistency

## Fingerprinting Techniques

Browser fingerprinting creates unique identifiers based on various browser characteristics:

### Components Used in Fingerprinting

- Navigator properties
- Screen resolution
- Available fonts
- WebGL information
- Canvas fingerprinting
- Audio context fingerprinting

### Tools and Libraries

- FingerprintJS
- Chrome DevTools Protocol
- Custom fingerprinting solutions

### Modification Techniques

Using Chrome DevTools Protocol `execute_cdp_cmd`, you can modify:

- Geolocation data
- Platform information
- Hardware concurrency
- Device memory

### Demonstration

To showcase browser fingerprint modification capabilities:

1. Execute the [demonstration](./examples/fingerprint_changer.py) script:
   ```bash
   python fingerprint_changer.py
   ```

2. The script will automatically:
   - Launch a browser session
   - Navigate to our fingerprint detection page
   - Display your current browser fingerprint in the terminal
   - Execute fingerprint modification commands
   - Show the new, modified fingerprint

This demonstration illustrates how browser fingerprints can be programmatically altered using Chrome DevTools Protocol commands, which is useful for avoiding fingerprint-based detection systems.

## Cookies and Sessions

Cookie and session management is crucial for successful scraping:

### Key Considerations

1. Session Management
   - Cookie persistence
   - Session identification
   - Authentication tokens

2. Detection Patterns
   - Clean browser signatures
   - Cookie patterns
   - Session behaviors

3. Best Practices

   - Maintain realistic cookie profiles
   - Implement session rotation
   - Use proper cookie management
   - Consider cross-domain cookies


## References

- Chrome DevTools Protocol Documentation: [Official Documentation](https://chromedevtools.github.io/devtools-protocol/)
- Selenium Documentation: [Official Selenium Docs](https://www.selenium.dev/documentation/)
- HTTP Protocol Specification: [RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616)
