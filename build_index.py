# -*- coding: utf-8 -*-
"""
Generator for REWAVE Landing Page (index.html)
"""

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml"
        href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='50' fill='%23C2D64D'/%3E%3C/svg%3E">
    <title>REWAVE — Everyday Functional Wellness | Kiwi Cucumber</title>

    <!-- Google Fonts: Anton, Caveat & Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Anton&family=Caveat:wght@500;600;700&family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap"
        rel="stylesheet">

    <style>
        :root {
            --forest-green: #12261C;
            --warm-bone: #F3EFE6;
            --moss-green: #8C9A5B;
            --lime-accent: #C2D64D;
            --warm-amber: #D9962F;
            --sage-bg: #B5C1B0;
            --sage-surface: #C6D1C2;
            --border-subtle: rgba(18, 38, 28, 0.12);
            --font-display: 'Anton', 'Impact', sans-serif;
            --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-script: 'Caveat', cursive, sans-serif;
            --font-accent: 'Instrument Serif', Georgia, serif;
            --stage-fg: var(--forest-green);
            --stage-fg-muted: rgba(18, 38, 28, 0.78);
            --stage-border: rgba(18, 38, 28, 0.14);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: auto;
            background-color: var(--sage-bg);
        }

        html.lenis,
        html.lenis body {
            height: auto;
        }

        .lenis.lenis-smooth {
            scroll-behavior: auto !important;
        }

        .lenis.lenis-smooth [data-lenis-prevent] {
            overscroll-behavior: contain;
        }

        .lenis.lenis-stopped {
            overflow: hidden;
        }

        .lenis.lenis-scrolling iframe {
            pointer-events: none;
        }

        body {
            background-color: var(--sage-bg);
            color: var(--forest-green);
            font-family: var(--font-body);
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            position: relative;
        }

        /* Tactile paper grain texture overlay */
        .paper-grain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 999;
            opacity: 0.038;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        }

        /* Unified Background Stage - Fixed, transitions smoothly between sage, bone and forest */
        #stage-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: var(--sage-bg);
            z-index: 1;
            pointer-events: none;
            transition: background-color 0.85s cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* 3D WebGL Canvas Layer - Above background stage, below navigation and active text */
        #webgl-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 5;
            pointer-events: none;
        }

        /* Floating Minimal Navigation */
        nav.nav-ui {
            position: fixed;
            top: 1.8rem;
            left: 2rem;
            right: 2rem;
            max-width: 1440px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
            pointer-events: auto;
        }

        .nav-left {
            display: flex;
            align-items: center;
            gap: 1rem;
            z-index: 2;
        }

        /* Center Brand Logo (Single persistent vector SVG transitioning from Hero to Header on scroll) */
        .nav-center-brand {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            align-items: center;
            justify-content: center;
            pointer-events: auto;
            z-index: 10;
        }

        .nav-brand-link {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            cursor: pointer;
        }

        .main-brand-logo-svg {
            height: 28px;
            width: 163px;
            display: block;
            color: var(--forest-green);
            fill: currentColor;
            transform-origin: center center;
            will-change: transform;
            user-select: none;
        }

        .nav-right {
            display: flex;
            align-items: center;
            z-index: 2;
        }

        /* Nav Buttons & Retouched Pill Elements */
        .nav-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            text-decoration: none;
            padding: 0.65rem 1.45rem;
            border-radius: 40px;
            font-family: var(--font-body);
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            cursor: pointer;
            border: 1px solid transparent;
            outline: none;
            position: relative;
            will-change: transform;
            transition: background 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease, color 0.3s ease;
        }

        .menu-btn {
            background: rgba(243, 239, 230, 0.45);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-color: rgba(18, 38, 28, 0.12);
            color: var(--forest-green);
            box-shadow: 0 4px 16px rgba(18, 38, 28, 0.04);
        }

        .menu-btn:hover {
            background: rgba(243, 239, 230, 0.8);
            border-color: var(--forest-green);
            transform: translateY(-1px);
        }

        .shop-btn {
            background: var(--forest-green);
            color: var(--warm-bone);
            box-shadow: 0 4px 16px rgba(18, 38, 28, 0.15);
            border-color: rgba(243, 239, 230, 0.15);
        }

        .shop-btn:hover {
            background: #1b3627;
            transform: translateY(-1px);
            box-shadow: 0 8px 24px rgba(18, 38, 28, 0.22);
        }

        .hamburger-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 18px;
            height: 18px;
        }

        .hamburger-icon svg {
            width: 18px;
            height: 18px;
            stroke: currentColor;
        }

        .btn-arrow-circle {
            width: 22px;
            height: 22px;
            border-radius: 50%;
            background: rgba(243, 239, 230, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease, background 0.3s ease;
        }

        .shop-btn:hover .btn-arrow-circle {
            transform: translateX(3px);
            background: rgba(243, 239, 230, 0.35);
        }

        .btn-arrow-circle svg {
            width: 12px;
            height: 12px;
        }

        .nav-socials {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-left: 0.5rem;
        }

        .social-link {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(243, 239, 230, 0.35);
            border: 1px solid rgba(18, 38, 28, 0.08);
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--forest-green);
            text-decoration: none;
            transition: background 0.3s ease, color 0.3s ease, transform 0.3s ease, border-color 0.3s ease;
        }

        .social-link:hover {
            background: var(--forest-green);
            color: var(--warm-bone);
            transform: translateY(-2px);
            border-color: var(--forest-green);
        }

        .social-link svg {
            width: 16px;
            height: 16px;
            fill: currentColor;
        }

        /* Kinetic Roll Text Engine */
        .kinetic-text {
            position: relative;
            display: inline-block;
            overflow: hidden;
            line-height: 1.1;
        }

        .kinetic-char {
            display: inline-block;
            transform-origin: 50% 50% -12px;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
        }

        .char-primary {
            display: inline-block;
        }

        .char-secondary {
            position: absolute;
            top: 0;
            left: 0;
            display: inline-block;
            transform: translateY(105%) rotateX(-90deg);
            opacity: 0;
        }

        .nav-btn:hover .kinetic-char {
            transform: translateY(-105%) rotateX(90deg);
            opacity: 0;
        }

        .nav-btn:hover .char-secondary {
            transform: translateY(0) rotateX(0deg);
            opacity: 1;
        }

        /* --- HERO SECTION --- */
        .hero {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding-top: calc(70px + 2.5rem);
            position: relative;
            z-index: 10;
            overflow: hidden;
            background: transparent;
        }

        /* Hero Content Grid: Left 3D bottle area, Right narrative */
        .hero-body {
            position: relative;
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            max-width: 1540px;
            width: 90%;
            margin: auto auto;
            min-height: 58vh;
            align-items: center;
            z-index: 15;
            pointer-events: none;
        }

        /* Left Side: Editorial Benefit Callouts positioned around 3D bottle */
        .product-callouts {
            position: relative;
            width: 100%;
            height: 100%;
            min-height: 480px;
            pointer-events: auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Hand-Drawn Cursive Editorial Annotations & Organic SVG Arrows */
        .cursive-annotation {
            position: absolute;
            display: flex;
            pointer-events: none;
            z-index: 16;
            transition: transform 0.3s ease;
        }

        .note-kiwi {
            top: 6%;
            left: 2%;
            flex-direction: column;
            align-items: flex-start;
            gap: 0.35rem;
        }

        .note-kiwi .cursive-text {
            font-size: clamp(1.35rem, 2.1vw, 1.7rem);
        }

        .note-sugar {
            top: 50%;
            right: 2%;
            left: auto;
            transform: translateY(-50%);
            flex-direction: row;
            align-items: center;
            gap: 0.6rem;
        }

        .note-sugar .cursive-text {
            font-size: clamp(1.35rem, 2.1vw, 1.7rem);
        }

        .cursive-text {
            font-family: var(--font-script);
            font-size: 1.7rem;
            line-height: 1.1;
            color: var(--forest-green);
            letter-spacing: 0.01em;
            transform: rotate(-3.5deg);
            white-space: nowrap;
            text-shadow: 0 1px 1px rgba(243, 239, 230, 0.6);
        }

        .note-sugar .cursive-text {
            transform: rotate(-1.5deg);
            color: #173825;
            font-size: 1.65rem;
        }

        .cursive-arrow-svg {
            width: 60px;
            height: 48px;
            display: block;
            filter: drop-shadow(0 2px 4px rgba(18, 38, 28, 0.06));
            flex-shrink: 0;
        }

        /* Editorial Pill Callouts */
        .callout-pill {
            display: none !important;
            position: absolute;
            background: rgba(243, 239, 230, 0.72);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(18, 38, 28, 0.12);
            border-radius: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 0.8rem;
            cursor: default;
            transition: border-color 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
            box-shadow: 0 8px 24px rgba(18, 38, 28, 0.06);
            z-index: 15;
        }

        .callout-pill:hover {
            background: rgba(243, 239, 230, 0.95);
            border-color: var(--forest-green);
            box-shadow: 0 12px 32px rgba(18, 38, 28, 0.12);
        }

        .callout-pill .pill-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--lime-accent);
            margin-bottom: 0.35rem;
        }

        .callout-pill .pill-title {
            font-size: 0.75rem;
            font-weight: 700;
            line-height: 1.25;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: var(--forest-green);
        }

        .c1 {
            top: 22%;
            left: 0%;
            min-width: 105px;
        }

        .c2 {
            top: 82%;
            left: 6%;
            min-width: 105px;
        }

        .c3 {
            top: 76%;
            right: 4%;
            min-width: 110px;
        }

        /* Right Side: Heavy Grotesque Headline Column */
        .headline-column {
            pointer-events: auto;
            padding-left: 1.5rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .headline-tag {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            color: var(--forest-green);
            margin-bottom: 1.2rem;
        }

        .headline-tag::before {
            content: '';
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--lime-accent);
        }

        .main-headline {
            font-family: var(--font-display);
            font-size: clamp(4rem, 6.5vw, 7.2rem);
            line-height: 0.9;
            text-transform: uppercase;
            letter-spacing: 0.01em;
            margin-bottom: 1.8rem;
        }

        .headline-row {
            overflow: hidden;
            display: block;
        }

        .headline-word {
            display: block;
        }

        .color-forest {
            color: var(--forest-green);
        }

        .headline-dot {
            color: var(--lime-accent);
            display: inline-block;
        }

        .hero-desc {
            font-size: clamp(1rem, 1.2vw, 1.22rem);
            line-height: 1.55;
            max-width: 440px;
            font-weight: 500;
            color: rgba(18, 38, 28, 0.88);
            margin-bottom: 2.2rem;
        }

        .cta-group {
            display: flex;
            align-items: center;
            gap: 1.8rem;
        }

        .hero-cta {
            display: inline-flex;
            align-items: center;
            gap: 0.9rem;
            background: var(--forest-green);
            color: var(--warm-bone);
            text-decoration: none;
            padding: 1.05rem 2.4rem;
            border-radius: 50px;
            font-size: 0.92rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            box-shadow: 0 8px 24px rgba(18, 38, 28, 0.18);
            border: 1px solid rgba(243, 239, 230, 0.2);
            transition: background 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            will-change: transform;
        }

        .hero-cta:hover {
            background: #1b3627;
            border-color: rgba(243, 239, 230, 0.4);
            box-shadow: 0 14px 34px rgba(18, 38, 28, 0.26);
        }

        .cta-arrow-circle {
            width: 26px;
            height: 26px;
            border-radius: 50%;
            background: rgba(243, 239, 230, 0.18);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease, background 0.3s ease;
        }

        .hero-cta:hover .cta-arrow-circle {
            transform: translateX(4px);
            background: rgba(243, 239, 230, 0.3);
        }

        .cta-arrow-circle svg {
            width: 14px;
            height: 14px;
        }

        .hero-secondary-link {
            font-size: 0.88rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: var(--forest-green);
            text-decoration: underline;
            text-underline-offset: 6px;
            cursor: pointer;
            transition: opacity 0.3s ease;
        }

        .hero-secondary-link:hover {
            opacity: 0.65;
        }

        /* Refined Editorial Marquee Divider (Sleek, transparent, non-clipping) */
        .marquee-ribbon-wrap {
            position: relative;
            width: 100%;
            overflow: hidden;
            background: transparent;
            color: var(--forest-green);
            padding: 0.65rem 0;
            margin-top: 1.5rem;
            border-top: 1px solid rgba(18, 38, 28, 0.12);
            border-bottom: 1px solid rgba(18, 38, 28, 0.12);
            z-index: 4;
            pointer-events: none;
            display: flex;
            align-items: center;
        }

        .marquee-track {
            display: flex;
            align-items: center;
            gap: 2rem;
            white-space: nowrap;
            will-change: transform;
            animation: infiniteMarquee 32s linear infinite;
        }

        .marquee-item {
            display: inline-flex;
            align-items: center;
            gap: 2rem;
            font-family: var(--font-body);
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            line-height: 1;
            color: var(--forest-green);
            opacity: 0.85;
        }

        .marquee-item .accent-word {
            color: var(--forest-green);
            font-weight: 800;
        }

        .marquee-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--lime-accent);
            display: inline-block;
            margin: 0 0.5rem;
            vertical-align: middle;
        }

        @keyframes infiniteMarquee {
            from {
                transform: translateX(0);
            }

            to {
                transform: translateX(-50%);
            }
        }

        /* --- STORY A: "FUNCTIONAL BY DESIGN" PINNED STAGE --- */
        .story-a-section {
            position: relative;
            z-index: 10;
            min-height: 100vh;
            background: transparent;
            padding: 7rem 5% 6rem;
            display: flex;
            align-items: center;
        }

        .story-a-container {
            max-width: 1440px;
            margin: 0 auto;
            width: 100%;
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 4rem;
            align-items: center;
            pointer-events: none;
        }

        .story-a-content {
            pointer-events: auto;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }

        .section-tag {
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            color: var(--forest-green);
            opacity: 0.85;
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .section-tag::before {
            content: '';
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--lime-accent);
        }

        .section-title {
            font-family: var(--font-display);
            font-size: clamp(2.8rem, 4.8vw, 4.8rem);
            line-height: 0.95;
            text-transform: uppercase;
            letter-spacing: 0.01em;
            color: var(--forest-green);
            margin-bottom: 1rem;
        }

        .section-intro {
            font-size: 1.12rem;
            line-height: 1.6;
            max-width: 520px;
            color: rgba(18, 38, 28, 0.78);
            margin-bottom: 1.5rem;
        }

        /* 4 Sequential Benefit Statements */
        .story-a-statements {
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
            max-width: 560px;
        }

        .statement-item {
            background: rgba(255, 255, 255, 0.78);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(18, 38, 28, 0.08);
            border-radius: 18px;
            padding: 1.6rem 2rem;
            display: flex;
            gap: 1.8rem;
            align-items: flex-start;
            transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1), transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 18px rgba(18, 38, 28, 0.03);
            will-change: opacity, transform;
        }

        .statement-item.active {
            opacity: 1 !important;
            transform: translateX(8px);
            border-color: var(--forest-green);
            box-shadow: 0 12px 30px rgba(18, 38, 28, 0.09);
            background: #ffffff;
        }

        .statement-item.dimmed {
            opacity: 0.28 !important;
            transform: translateX(0);
        }

        .stmt-num {
            font-family: var(--font-display);
            font-size: 1.8rem;
            color: var(--forest-green);
            line-height: 1;
            flex-shrink: 0;
        }

        .stmt-content {
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }

        .stmt-title {
            font-family: var(--font-display);
            font-size: 1.45rem;
            text-transform: uppercase;
            letter-spacing: 0.03em;
            color: var(--forest-green);
        }

        .stmt-desc {
            font-size: 0.92rem;
            line-height: 1.5;
            color: rgba(18, 38, 28, 0.76);
        }

        .stmt-badge {
            align-self: flex-start;
            margin-top: 0.35rem;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--forest-green);
            background: rgba(194, 214, 77, 0.25);
            padding: 0.25rem 0.65rem;
            border-radius: 20px;
        }

        /* Clear right column reserved for the traveling 3D bottle */
        .story-a-bottle-stage {
            min-height: 500px;
            pointer-events: none;
        }

        /* --- STORY B: "RELEASE" PINNED STAGE --- */
        .story-b-section {
            position: relative;
            z-index: 10;
            min-height: 100vh;
            height: 100vh;
            background: transparent;
            padding: 0;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .story-b-grid-wrap {
            position: relative;
            width: 90%;
            max-width: 1540px;
            height: 100%;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding-top: calc(70px + 1.6rem);
            padding-bottom: 0;
            z-index: 15;
            pointer-events: none;
        }

        /* Top Area: Architectural Header */
        .story-b-header {
            position: relative;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            pointer-events: auto;
        }

        .story-b-meta-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .story-b-tag {
            display: inline-flex;
            align-items: center;
            gap: 0.65rem;
            font-size: 0.80rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--stage-fg, var(--forest-green));
            transition: color 0.4s ease;
        }

        .meta-coords {
            font-family: var(--font-body);
            font-size: 0.70rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--lime-accent);
            opacity: 0.85;
        }

        .story-b-headline {
            margin-top: 0.35rem;
            margin-bottom: 0;
            color: var(--stage-fg, var(--forest-green));
            transition: color 0.4s ease;
            text-shadow: none !important;
            display: flex;
            align-items: baseline;
            gap: 1.2rem;
            flex-wrap: wrap;
        }

        .story-b-title-main {
            display: inline-block;
            font-family: var(--font-display);
            font-size: clamp(2.8rem, 5.8vw, 5.8rem);
            line-height: 0.95;
            text-transform: uppercase;
            letter-spacing: -0.01em;
            color: var(--stage-fg, var(--forest-green));
            text-shadow: none !important;
        }

        .story-b-title-accent {
            display: inline-block;
            font-family: var(--font-accent, 'Instrument Serif', Georgia, serif);
            font-style: italic;
            font-weight: 400;
            font-size: clamp(1.8rem, 3.8vw, 3.8rem);
            line-height: 1.05;
            letter-spacing: 0.01em;
            color: var(--stage-fg, var(--forest-green));
            opacity: 0;
            transform: translateY(10px);
            will-change: opacity, transform;
            text-shadow: none !important;
        }

        /* Deconstructed Botanical Architecture Stage */
        .story-b-architecture {
            position: relative;
            width: 100%;
            flex: 1;
            display: grid;
            grid-template-columns: minmax(280px, 380px) minmax(200px, 320px) minmax(280px, 380px);
            justify-content: space-between;
            align-items: center;
            pointer-events: none;
            padding: 0.5rem 0;
            z-index: 10;
        }

        .deconstruct-col {
            display: flex;
            flex-direction: column;
            gap: 1.6rem;
            pointer-events: auto;
        }

        .deconstruct-center-void {
            pointer-events: none;
            width: 100%;
            height: 100%;
        }

        .deconstruct-node {
            position: relative;
            background: rgba(18, 38, 28, 0.48);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(243, 239, 230, 0.12);
            border-radius: 16px;
            padding: 1.25rem 1.45rem;
            opacity: 0;
            transform: translateY(18px);
            transition: border-color 0.4s ease, transform 0.4s ease, box-shadow 0.4s ease, opacity 0.4s ease, background 0.4s ease;
            cursor: pointer;
        }

        .deconstruct-node:hover,
        .deconstruct-node.active {
            border-color: rgba(194, 214, 77, 0.55);
            background: rgba(18, 38, 28, 0.72);
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35), 0 0 24px rgba(194, 214, 77, 0.12);
            transform: translateY(-2px);
        }

        .node-meta {
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .node-index {
            font-family: var(--font-body);
            font-size: 0.70rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            color: var(--forest-green);
            background: var(--lime-accent);
            padding: 0.15rem 0.45rem;
            border-radius: 4px;
        }

        .node-system {
            font-family: var(--font-body);
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--lime-accent);
        }

        .node-title {
            font-family: var(--font-body);
            font-size: clamp(0.98rem, 1.15vw, 1.18rem);
            font-weight: 700;
            letter-spacing: -0.01em;
            color: var(--stage-fg, var(--warm-bone));
            margin: 0.4rem 0 0.35rem;
            transition: color 0.4s ease;
        }

        .node-desc {
            font-family: var(--font-body);
            font-size: clamp(0.78rem, 0.88vw, 0.88rem);
            line-height: 1.55;
            color: var(--stage-fg-muted, rgba(243, 239, 230, 0.78));
            margin: 0;
            font-weight: 450;
            transition: color 0.4s ease;
        }

        .node-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-top: 0.65rem;
        }

        .node-tag {
            font-family: var(--font-body);
            font-size: 0.64rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 0.18rem 0.55rem;
            border-radius: 30px;
            background: rgba(243, 239, 230, 0.06);
            border: 1px solid rgba(243, 239, 230, 0.12);
            color: var(--stage-fg, var(--warm-bone));
            transition: border-color 0.3s ease, background 0.3s ease;
        }

        .deconstruct-node:hover .node-tag,
        .deconstruct-node.active .node-tag {
            border-color: rgba(194, 214, 77, 0.3);
            background: rgba(194, 214, 77, 0.08);
            color: var(--warm-bone);
        }

        /* Minimalist Hairline Connectors */
        .node-pointer {
            position: absolute;
            top: 50%;
            display: flex;
            align-items: center;
            pointer-events: none;
            opacity: 0.55;
            transition: opacity 0.4s ease;
        }

        .deconstruct-node:hover .node-pointer,
        .deconstruct-node.active .node-pointer {
            opacity: 1;
        }

        .pointer-right {
            right: -32px;
            transform: translateY(-50%);
        }

        .pointer-left {
            left: -32px;
            transform: translateY(-50%);
        }

        .pointer-line {
            width: 26px;
            height: 1px;
            background: linear-gradient(to right, rgba(194, 214, 77, 0.8), rgba(194, 214, 77, 0.15));
        }

        .pointer-left .pointer-line {
            background: linear-gradient(to left, rgba(194, 214, 77, 0.8), rgba(194, 214, 77, 0.15));
        }

        .pointer-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--lime-accent);
            box-shadow: 0 0 8px rgba(194, 214, 77, 0.8);
            flex-shrink: 0;
        }

        /* Bottom Edge: Hairline-Separated Spec Strip */
        .story-b-spec-strip {
            position: relative;
            width: 100%;
            padding: 1.1rem 0 1.3rem;
            border-top: 1px solid var(--stage-border, rgba(18, 38, 28, 0.14));
            display: flex;
            justify-content: space-between;
            align-items: center;
            opacity: 0;
            pointer-events: auto;
            transition: border-color 0.4s ease;
        }

        .spec-item {
            display: flex;
            align-items: center;
        }

        .spec-text {
            font-family: var(--font-body);
            font-weight: 700;
            font-size: clamp(0.72rem, 0.90vw, 0.85rem);
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--stage-fg, var(--forest-green));
            transition: color 0.4s ease;
        }

        .spec-dot {
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background-color: var(--lime-accent);
            display: inline-block;
            margin: 0 1.2rem;
            flex-shrink: 0;
        }

        @media (max-width: 1024px) {
            .story-b-architecture {
                grid-template-columns: 1fr;
                gap: 1.2rem;
                padding-top: 0.4rem;
            }

            .deconstruct-col {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.0rem;
            }

            .deconstruct-center-void {
                display: none;
            }

            .node-pointer {
                display: none;
            }
        }

        @media (max-width: 768px) {
            .story-b-grid-wrap {
                padding-top: calc(70px + 1.0rem);
            }

            .meta-coords {
                display: none;
            }

            .story-b-architecture {
                grid-template-columns: 1fr;
                gap: 0.75rem;
            }

            .deconstruct-col {
                display: flex;
                flex-direction: column;
                gap: 0.75rem;
            }

            .deconstruct-node {
                padding: 1.0rem 1.15rem;
            }

            .node-title {
                font-size: 1.0rem;
            }

            .node-desc {
                font-size: 0.80rem;
                line-height: 1.48;
            }

            .story-b-spec-strip {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 0.75rem 1.0rem;
                padding: 1.0rem 0 1.2rem;
            }

            .story-b-spec-strip .spec-dot {
                display: none;
            }

            .spec-item {
                justify-content: flex-start;
            }
        }

        @media (prefers-reduced-motion: reduce) {

            .story-b-title-accent,
            .story-b-spec-strip,
            .deconstruct-node {
                transform: none !important;
                transition: opacity 0.01ms !important;
            }
        }

        /* --- DAILY RITUALS SECTION --- */
        .rituals-section {
            position: relative;
            z-index: 10;
            background: transparent;
            color: var(--warm-bone);
            padding: 8rem 5% 6rem;
        }

        .rituals-container {
            max-width: 1360px;
            margin: 0 auto;
        }

        .rituals-header {
            margin-bottom: 4rem;
        }

        .rituals-title {
            font-family: var(--font-display);
            font-size: clamp(2.8rem, 5.2vw, 5.2rem);
            line-height: 0.94;
            text-transform: uppercase;
            letter-spacing: -0.01em;
            color: var(--warm-bone);
            margin-top: 0.6rem;
        }

        .rituals-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2.2rem;
        }

        .ritual-item {
            background: rgba(243, 239, 230, 0.035);
            border: 1px solid rgba(243, 239, 230, 0.12);
            border-radius: 16px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .ritual-item:hover {
            background: rgba(243, 239, 230, 0.07);
            border-color: rgba(194, 214, 77, 0.40);
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.30);
        }

        .ritual-img-wrap {
            position: relative;
            width: 100%;
            height: 240px;
            overflow: hidden;
            background: rgba(18, 38, 28, 0.6);
        }

        .ritual-img-wrap::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(14, 28, 20, 0.05) 0%, rgba(14, 28, 20, 0.68) 100%);
            pointer-events: none;
            transition: opacity 0.4s ease;
            z-index: 1;
        }

        .ritual-item:hover .ritual-img-wrap::after {
            opacity: 0.45;
        }

        .ritual-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
            filter: brightness(0.92) contrast(1.05);
        }

        .ritual-item:hover .ritual-img {
            transform: scale(1.06);
            filter: brightness(0.98) contrast(1.05);
        }

        .ritual-badge {
            position: absolute;
            top: 1.1rem;
            left: 1.1rem;
            background: rgba(18, 38, 28, 0.82);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(243, 239, 230, 0.22);
            border-radius: 20px;
            padding: 0.35rem 0.85rem;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.10em;
            color: var(--lime-accent);
            z-index: 2;
        }

        .ritual-img-overlay-tag {
            position: absolute;
            bottom: 1.1rem;
            left: 1.25rem;
            color: var(--warm-bone);
            font-size: 1.05rem;
            font-weight: 500;
            letter-spacing: 0.02em;
            z-index: 2;
            pointer-events: none;
            display: flex;
            align-items: baseline;
            gap: 0.35rem;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
        }

        .ritual-img-overlay-tag em {
            font-family: var(--font-accent);
            font-style: italic;
            font-size: 1.35rem;
            color: var(--lime-accent);
            line-height: 1;
        }

        .ritual-content {
            padding: 2rem;
            display: flex;
            flex-direction: column;
            flex: 1;
            justify-content: space-between;
        }

        .ritual-time {
            font-size: 0.80rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.14em;
            color: var(--lime-accent);
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
        }

        .ritual-heading {
            font-family: var(--font-display);
            font-size: 2.0rem;
            line-height: 1.05;
            letter-spacing: 0.01em;
            text-transform: uppercase;
            margin-bottom: 0.8rem;
            color: var(--warm-bone);
        }

        .ritual-text {
            font-size: 0.95rem;
            line-height: 1.65;
            color: rgba(243, 239, 230, 0.78);
        }

        /* --- NUTRITIONAL TRANSPARENCY: "READ THE LABEL" --- */
        .transparency-section {
            position: relative;
            z-index: 10;
            background: transparent;
            color: var(--warm-bone);
            padding: 6rem 5% 8rem;
            border-top: 1px solid rgba(243, 239, 230, 0.12);
        }

        .transparency-container {
            max-width: 1360px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            gap: 4.5rem;
            align-items: center;
        }

        .transparency-title {
            font-family: var(--font-display);
            font-size: clamp(2.8rem, 5.0vw, 5.0rem);
            line-height: 0.94;
            text-transform: uppercase;
            letter-spacing: -0.01em;
            color: var(--warm-bone);
            margin-top: 0.6rem;
            margin-bottom: 1.4rem;
        }

        .transparency-desc {
            font-size: 1.05rem;
            line-height: 1.65;
            color: rgba(243, 239, 230, 0.80);
            max-width: 480px;
            margin-bottom: 2.2rem;
        }

        .fssai-verification-badge {
            display: inline-flex;
            align-items: center;
            gap: 1.2rem;
            background: rgba(243, 239, 230, 0.05);
            border: 1px solid rgba(243, 239, 230, 0.16);
            border-radius: 12px;
            padding: 1rem 1.6rem;
        }

        .fssai-mark {
            font-family: var(--font-display);
            font-size: 1.6rem;
            color: var(--lime-accent);
            letter-spacing: 0.05em;
        }

        .fssai-details {
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
        }

        .fssai-lbl {
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--warm-bone);
        }

        .fssai-lic {
            font-size: 0.7rem;
            color: rgba(243, 239, 230, 0.6);
            letter-spacing: 0.04em;
        }

        /* Clean Nutritional Facts Card */
        .nutrition-card {
            background: rgba(11, 23, 17, 0.65);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(243, 239, 230, 0.16);
            border-radius: 16px;
            padding: 2.4rem;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
        }

        .nutrition-card-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 2px solid var(--warm-bone);
            padding-bottom: 0.8rem;
            margin-bottom: 1.2rem;
        }

        .card-title {
            font-family: var(--font-display);
            font-size: 1.55rem;
            letter-spacing: 0.03em;
            color: var(--warm-bone);
        }

        .card-serve {
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.10em;
            color: var(--lime-accent);
        }

        .nutrition-table {
            display: flex;
            flex-direction: column;
        }

        .nutri-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.72rem 0;
            border-bottom: 1px solid rgba(243, 239, 230, 0.10);
            font-size: 0.95rem;
            color: var(--warm-bone);
        }

        .nutri-row.sub-row {
            padding-left: 1.2rem;
            color: rgba(243, 239, 230, 0.75);
            font-size: 0.88rem;
        }

        .nutri-name {
            font-weight: 500;
        }

        .nutri-val {
            font-weight: 700;
            letter-spacing: 0.02em;
        }

        .highlight-val {
            color: var(--lime-accent);
        }

        .nutrition-card-footer {
            margin-top: 1.4rem;
            padding-top: 1.2rem;
            border-top: 1px solid rgba(243, 239, 230, 0.15);
        }

        .ingredients-header {
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            color: var(--lime-accent);
            margin-bottom: 0.4rem;
        }

        .ingredients-list {
            font-size: 0.88rem;
            line-height: 1.55;
            color: rgba(243, 239, 230, 0.75);
        }

        @media (max-width: 1024px) {
            .rituals-grid {
                grid-template-columns: 1fr;
                gap: 1.8rem;
            }

            .transparency-container {
                grid-template-columns: 1fr;
                gap: 3.5rem;
            }
        }

        /* --- REBUILT EDITORIAL BRAND FOOTER --- */
        .site-footer {
            position: relative;
            z-index: 10;
            background-color: #0F2B1F;
            color: #F3EFE6;
            width: 100%;
            overflow: hidden;
            padding: 0 0 3.5rem;
            container-type: inline-size;
        }

        .footer-landscape-container {
            width: 100%;
            overflow: hidden;
            line-height: 0;
            position: relative;
        }

        .footer-landscape-picture {
            display: block;
            width: 100%;
        }

        .footer-landscape-img {
            width: 100%;
            height: auto;
            display: block;
            transform-origin: center bottom;
            will-change: transform;
        }

        /* Pull content up so headline sits comfortably in the solid #0F2B1F area (never over the hills) */
        .footer-content {
            position: relative;
            z-index: 2;
            margin-top: calc(-0.38 * (724 / 2172 * 100cqw) + 40px);
        }

        @media (max-width: 768px) {
            .footer-content {
                margin-top: calc(-0.38 * (724 / 940 * 100cqw) + 40px);
            }
        }

        .footer-headline-wrap {
            max-width: 1360px;
            margin: 0 auto 4.5rem;
            padding: 0 5%;
        }

        .footer-headline {
            display: flex;
            flex-direction: column;
            line-height: 0.94;
            gap: 0.15rem;
        }

        .footer-headline-mask {
            display: block;
            overflow: hidden;
        }

        .footer-headline-line {
            display: block;
            will-change: transform;
        }

        .footer-headline-anton {
            font-family: var(--font-display, 'Anton', sans-serif);
            font-size: clamp(44px, 6vw, 84px);
            text-transform: uppercase;
            letter-spacing: -0.01em;
            color: #F3EFE6;
        }

        .footer-headline-serif {
            font-family: var(--font-accent, 'Instrument Serif', Georgia, serif);
            font-style: italic;
            text-transform: none;
            font-size: clamp(44px, 6vw, 84px);
            letter-spacing: -0.01em;
            color: #F3EFE6;
            font-weight: 400;
        }

        .footer-main-row {
            max-width: 1360px;
            margin: 0 auto;
            padding: 0 5%;
            display: grid;
            grid-template-columns: 1.2fr 0.8fr 0.8fr 1.6fr;
            gap: 3.5rem;
            align-items: flex-start;
        }

        .footer-nav-pair {
            display: contents;
        }

        .footer-col {
            will-change: transform, opacity;
        }

        .footer-col-brand .footer-logo-svg {
            width: 160px;
            height: auto;
            max-height: 32px;
            fill: #F3EFE6;
            display: block;
            margin-bottom: 1.2rem;
        }

        .footer-copy-text {
            font-family: var(--font-body);
            font-size: 0.88rem;
            color: rgba(243, 239, 230, 0.70);
            letter-spacing: 0.04em;
        }

        .footer-col-title {
            font-family: var(--font-body);
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: #F3EFE6;
            margin-bottom: 1.2rem;
        }

        .footer-nav-list {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .footer-link {
            font-family: var(--font-body);
            color: rgba(243, 239, 230, 0.75);
            text-decoration: none;
            font-size: 0.92rem;
            transition: color 0.25s ease;
            display: inline-block;
        }

        .footer-link:hover {
            color: var(--lime-accent, #C2D64D);
        }

        .footer-newsletter-text {
            font-family: var(--font-body);
            font-size: 0.92rem;
            color: rgba(243, 239, 230, 0.75);
            line-height: 1.5;
            margin-bottom: 1.2rem;
        }

        .footer-form {
            width: 100%;
        }

        .footer-input-wrap {
            display: flex;
            align-items: center;
            background: rgba(243, 239, 230, 0.06);
            border: 1px solid rgba(243, 239, 230, 0.18);
            border-radius: 9999px;
            padding: 0.35rem 0.4rem 0.35rem 1.2rem;
            transition: border-color 0.25s ease, background 0.25s ease;
        }

        .footer-input-wrap:focus-within {
            border-color: var(--lime-accent, #C2D64D);
            background: rgba(243, 239, 230, 0.10);
        }

        .footer-email-input {
            flex: 1;
            background: transparent;
            border: none;
            outline: none;
            color: #F3EFE6;
            font-family: var(--font-body);
            font-size: 0.90rem;
            min-width: 0;
        }

        .footer-email-input::placeholder {
            color: rgba(243, 239, 230, 0.45);
        }

        .footer-submit-btn {
            background: var(--lime-accent, #C2D64D);
            color: #0F2B1F;
            font-family: var(--font-body);
            font-weight: 700;
            font-size: 0.78rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 0.75rem 1.4rem;
            border-radius: 9999px;
            border: none;
            cursor: pointer;
            white-space: nowrap;
            transition: background 0.25s ease, transform 0.2s ease;
        }

        .footer-submit-btn:hover {
            background: #d4e85d;
            transform: translateY(-1px);
        }

        .footer-form-feedback {
            display: none;
            color: #ff8585;
            font-family: var(--font-body);
            font-size: 0.82rem;
            margin-top: 0.6rem;
            padding-left: 0.5rem;
        }

        .footer-form-success {
            font-family: var(--font-body);
            font-size: 0.95rem;
            color: var(--lime-accent, #C2D64D);
            padding: 0.8rem 0;
            font-weight: 600;
        }

        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }

        /* Hairline Bottom Row */
        .footer-bottom-row {
            max-width: 1360px;
            margin: 4.5rem auto 0;
            padding: 1.8rem 5% 0;
            border-top: 1px solid rgba(243, 239, 230, 0.12);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: rgba(243, 239, 230, 0.70);
            flex-wrap: wrap;
            gap: 1rem;
        }

        /* Visible Focus Rings */
        .footer-link:focus-visible,
        .footer-submit-btn:focus-visible,
        .footer-email-input:focus-visible {
            outline: 2px solid var(--lime-accent, #C2D64D);
            outline-offset: 3px;
        }

        /* Responsive Breakpoint (768px) */
        @media (max-width: 768px) {
            .footer-headline-wrap {
                margin-bottom: 3.5rem;
            }

            .footer-main-row {
                display: flex;
                flex-direction: column;
                gap: 2.8rem;
            }

            .footer-nav-pair {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 2rem;
                width: 100%;
            }

            .footer-col-newsletter {
                width: 100%;
            }

            .footer-input-wrap {
                padding: 0.3rem 0.35rem 0.3rem 1rem;
            }

            .footer-bottom-row {
                margin-top: 3.5rem;
                flex-direction: column;
                align-items: flex-start;
                gap: 0.6rem;
            }
        }

        /* --- OFF-CANVAS OVERLAY MENU --- */
        .menu-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 200;
            pointer-events: none;
            visibility: hidden;
            overflow: hidden;
        }

        .menu-overlay.is-active {
            pointer-events: auto;
            visibility: visible;
        }

        .overlay-backdrop {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(14, 28, 20, 0.82);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            opacity: 0;
            cursor: pointer;
        }

        .overlay-panel {
            position: absolute;
            top: 0;
            right: 0;
            width: min(92vw, 620px);
            height: 100%;
            max-height: 100vh;
            background: var(--forest-green);
            color: var(--warm-bone);
            box-shadow: -24px 0 70px rgba(0, 0, 0, 0.55);
            transform: translateX(100%);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 2.8rem 3.5rem;
            overflow-y: auto;
            overflow-x: hidden;
            scrollbar-width: none;
            -ms-overflow-style: none;
            z-index: 2;
        }

        .overlay-panel::-webkit-scrollbar {
            display: none;
        }

        .overlay-header {
            position: relative;
            z-index: 10;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 1.6rem;
            border-bottom: 1px solid rgba(243, 239, 230, 0.12);
            flex-shrink: 0;
        }

        .overlay-brand {
            display: flex;
            align-items: baseline;
            gap: 1.2rem;
        }

        .overlay-logo-svg {
            width: 125px;
            height: 21px;
            fill: var(--warm-bone);
            display: block;
        }

        .overlay-tag {
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--lime-accent);
        }

        .overlay-close-btn {
            background: rgba(243, 239, 230, 0.08);
            border: 1px solid rgba(243, 239, 230, 0.16);
            color: var(--warm-bone);
            padding: 0.6rem 1.25rem;
            border-radius: 40px;
            font-family: var(--font-body);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.65rem;
            white-space: nowrap !important;
            flex-shrink: 0;
            line-height: 1;
            transition: background 0.3s ease, border-color 0.3s ease, transform 0.3s ease;
        }

        .overlay-close-btn:hover {
            background: rgba(243, 239, 230, 0.2);
            border-color: var(--warm-bone);
            transform: translateY(-1px);
        }

        .overlay-close-btn .kinetic-text {
            white-space: nowrap !important;
            display: inline-flex;
            line-height: 1;
        }

        .overlay-close-btn .kinetic-char {
            white-space: pre;
            display: inline-block;
        }

        .close-icon-circle {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: rgba(243, 239, 230, 0.12);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease, background 0.3s ease;
        }

        .close-icon-circle svg {
            width: 11px;
            height: 11px;
        }

        .overlay-close-btn:hover .close-icon-circle {
            transform: rotate(90deg);
            background: var(--lime-accent);
            color: var(--forest-green);
        }

        .overlay-body {
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin: 2rem 0;
            flex: 1;
        }

        .overlay-nav {
            width: 100%;
        }

        .overlay-menu-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: clamp(1.1rem, 2.5vh, 1.85rem);
        }

        .menu-item {
            position: relative;
        }

        .menu-link {
            text-decoration: none;
            color: var(--warm-bone);
            display: inline-flex;
            align-items: center;
            gap: clamp(1rem, 2.2vw, 1.6rem);
            position: relative;
            white-space: nowrap !important;
            padding: 0.25rem 0;
            transition: color 0.3s ease;
        }

        .menu-num {
            font-family: var(--font-body);
            font-size: 0.85rem;
            font-weight: 800;
            letter-spacing: 0.16em;
            color: var(--lime-accent);
            opacity: 0.9;
            min-width: 28px;
            transition: transform 0.3s ease, color 0.3s ease;
        }

        .menu-title {
            font-family: var(--font-display);
            font-size: clamp(1.85rem, 3.1vw, 2.75rem);
            line-height: 1;
            letter-spacing: 0.03em;
            text-transform: uppercase;
            color: var(--warm-bone);
            white-space: nowrap !important;
            transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), color 0.3s ease;
        }

        .menu-arrow-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transform: translateX(-10px);
            transition: opacity 0.3s ease, transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            color: var(--lime-accent);
            margin-left: 0.35rem;
        }

        .menu-arrow-icon svg {
            width: 22px;
            height: 22px;
        }

        .menu-item:hover .menu-title {
            color: var(--lime-accent);
            transform: translateX(10px);
        }

        .menu-item:hover .menu-num {
            color: #ffffff;
            transform: translateX(4px);
        }

        .menu-item:hover .menu-arrow-icon {
            opacity: 1;
            transform: translateX(8px);
        }

        .overlay-footer {
            position: relative;
            z-index: 10;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding-top: 1.6rem;
            border-top: 1px solid rgba(243, 239, 230, 0.12);
            gap: 1.5rem;
            flex-shrink: 0;
        }

        .overlay-footer-col {
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
        }

        .overlay-footer-col .footer-label {
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--lime-accent);
        }

        .overlay-footer-col .footer-email {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--warm-bone);
            text-decoration: none;
            font-size: 0.88rem;
            font-weight: 600;
            transition: color 0.25s ease;
        }

        .overlay-footer-col .footer-email:hover {
            color: var(--lime-accent);
        }

        .overlay-socials {
            display: flex;
            align-items: center;
            gap: 0.45rem;
            font-size: 0.82rem;
            color: var(--warm-bone);
        }

        .overlay-socials a {
            color: var(--warm-bone);
            text-decoration: none;
            transition: color 0.25s ease;
        }

        .overlay-socials a:hover {
            color: var(--lime-accent);
        }

        .overlay-socials .separator {
            color: rgba(243, 239, 230, 0.35);
        }

        .overlay-footer-col .footer-status {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            font-size: 0.82rem;
            font-weight: 600;
            color: rgba(243, 239, 230, 0.88);
        }

        .overlay-footer-col .status-indicator {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--lime-accent);
            box-shadow: 0 0 10px var(--lime-accent);
        }

        /* ===================================================
           COMPREHENSIVE RESPONSIVE STYLES (TABLET & MOBILE)
           =================================================== */

        /* Prevent canvas horizontal overflow jitter */
        #stage-bg,
        #webgl-container {
            width: 100%;
            height: 100%;
            inset: 0;
        }

        /* --- Tablet Landscape & Standard Tablet (<= 1024px) --- */
        @media (max-width: 1024px) {
            .hero-body {
                grid-template-columns: 1fr;
                gap: 1.5rem;
                padding-top: 1.5rem;
            }

            .product-callouts {
                min-height: 320px;
            }

            .headline-column {
                padding-left: 0;
                text-align: center;
                align-items: center;
            }

            .story-a-container {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .rituals-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .transparency-container {
                grid-template-columns: 1fr;
                gap: 3rem;
            }

            .overlay-body {
                grid-template-columns: 1fr;
            }

            .overlay-panel {
                padding: 2.5rem 2rem;
                width: 100vw;
            }
        }

        /* --- Tablet Portrait & Large Mobile (<= 860px) --- */
        @media (max-width: 860px) {
            .nav-socials {
                display: none !important;
            }
        }

        /* --- Standard Mobile (<= 768px) --- */
        @media (max-width: 768px) {

            /* Navigation */
            nav.nav-ui {
                left: 1rem;
                right: 1rem;
                top: 1rem;
            }

            .main-brand-logo-svg {
                width: 120px;
                height: 20px;
            }

            .nav-btn {
                padding: 0.55rem 0.95rem;
                font-size: 0.72rem;
                gap: 0.45rem;
            }

            /* Hero spacing on mobile */
            .hero {
                padding-top: 5.5rem;
            }

            /* Hero Layout & Typography */
            .hero-body {
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
                gap: 1rem;
                padding-top: 0.5rem;
                min-height: auto;
            }

            .product-callouts {
                min-height: 280px;
                width: 100%;
                order: 1;
            }

            .headline-column {
                order: 2;
                align-items: center;
                text-align: center;
                padding: 0;
                width: 100%;
            }

            .cursive-annotation {
                display: flex !important;
            }

            .note-kiwi {
                top: 4%;
                left: 3%;
                gap: 0.2rem;
            }

            .note-kiwi .cursive-text {
                font-size: 1.15rem;
                line-height: 1.05;
            }

            .note-sugar {
                top: 50%;
                right: 3%;
                left: auto;
                transform: translateY(-50%);
                gap: 0.35rem;
            }

            .note-sugar .cursive-text {
                font-size: 1.15rem;
                line-height: 1.05;
            }

            .cursive-arrow-svg {
                width: 44px;
                height: 36px;
            }

            .main-headline {
                font-size: clamp(2.2rem, 8.5vw, 3.4rem);
                line-height: 0.95;
            }

            .hero-desc {
                font-size: clamp(0.92rem, 3.2vw, 1.1rem);
                line-height: 1.5;
                max-width: 100%;
                margin-top: 0.6rem;
            }

            .cta-group {
                flex-direction: column;
                width: 100%;
                max-width: 320px;
                margin: 0 auto;
                gap: 0.75rem;
            }

            .hero-cta-main,
            .hero-cta-secondary {
                width: 100%;
                justify-content: center;
            }

            /* Story A: The Botanical Matrix (Interactive Showcase Mode) */
            .story-a-section {
                padding: 5.5rem 1.2rem 2rem;
                height: 100vh;
                min-height: 100vh;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
            }

            .story-a-container {
                display: flex;
                flex-direction: column;
                height: 100%;
                justify-content: space-between;
                gap: 0;
            }

            .story-a-content {
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                gap: 0;
            }

            .story-a-header {
                text-align: center;
                z-index: 10;
            }

            .story-a-header .section-tag {
                justify-content: center;
                font-size: 0.72rem;
                margin-bottom: 0.25rem;
            }

            .story-a-header .section-title {
                font-size: clamp(1.8rem, 6vw, 2.4rem);
                line-height: 1;
                margin: 0;
            }

            .story-a-header .section-intro {
                display: none;
            }

            .story-a-bottle-stage {
                display: block;
                min-height: 220px;
                flex: 1;
            }

            .story-a-statements {
                position: relative;
                width: 100%;
                max-width: 100%;
                min-height: 180px;
                z-index: 10;
                margin-bottom: 1rem;
            }

            .story-a-statements .statement-item {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                opacity: 0 !important;
                pointer-events: none;
                transform: translateY(12px) scale(0.98);
                transition: opacity 0.4s ease, transform 0.4s ease;
                padding: 1.1rem 1.3rem;
                gap: 1rem;
                border-radius: 14px;
            }

            .story-a-statements .statement-item.active {
                opacity: 1 !important;
                pointer-events: auto;
                transform: translateY(0) scale(1);
            }

            .statement-item .stmt-num {
                font-size: 1.4rem;
            }

            .statement-item .stmt-title {
                font-size: 1.1rem;
            }

            .statement-item .stmt-desc {
                font-size: 0.85rem;
                line-height: 1.45;
            }

            .statement-item .stmt-badge {
                font-size: 0.68rem;
                padding: 0.25rem 0.65rem;
            }

            /* Story B: The Moment of Release */
            .story-b-grid-wrap {
                padding-top: calc(60px + 1rem);
                padding-bottom: 0.8rem;
                width: 92%;
            }

            .story-b-title-main {
                font-size: clamp(2.8rem, 10vw, 4.2rem);
            }

            .story-b-title-accent {
                font-size: clamp(1.8rem, 6vw, 2.5rem);
            }

            .story-b-paragraph {
                font-size: 0.95rem;
                line-height: 1.45;
                max-width: 100%;
            }

            .story-b-spec-strip {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 0.6rem 1rem;
                padding: 0.8rem 0;
            }

            .story-b-spec-strip .spec-dot {
                display: none;
            }

            .spec-text {
                font-size: 0.72rem;
            }

            /* Rituals */
            .rituals-section {
                padding: 5rem 5% 4rem;
            }

            .rituals-title {
                font-size: clamp(2.2rem, 7.5vw, 3.6rem);
            }

            .ritual-img-wrap {
                height: 220px;
            }

            /* Transparency */
            .transparency-section {
                padding: 4.5rem 5% 5rem;
            }

            .transparency-title {
                font-size: clamp(2.2rem, 7.5vw, 3.6rem);
            }

            .nutrition-card {
                padding: 1.5rem 1.2rem;
            }

            .fssai-verification-badge {
                flex-wrap: wrap;
                gap: 0.8rem;
                padding: 0.8rem 1.2rem;
                max-width: 100%;
            }



            /* Overlay Menu Responsive */
            .overlay-panel {
                padding: 2rem 1.6rem 1.8rem;
                width: 100vw;
            }

            .overlay-header {
                padding-bottom: 1.2rem;
            }

            .overlay-body {
                margin: 1.5rem 0;
            }

            .overlay-menu-list {
                gap: clamp(0.9rem, 2.2vh, 1.4rem);
            }

            .menu-link {
                gap: 1.1rem;
            }

            .menu-title {
                font-size: clamp(1.45rem, 5.8vw, 2.0rem);
            }

            .overlay-footer {
                flex-direction: column;
                gap: 1rem;
                padding-top: 1.2rem;
            }
        }

        /* --- Small Mobile (<= 420px) --- */
        @media (max-width: 420px) {
            nav.nav-ui {
                left: 0.75rem;
                right: 0.75rem;
                top: 0.85rem;
            }

            .main-brand-logo-svg {
                width: 105px;
                height: 18px;
            }

            .nav-btn {
                padding: 0.5rem 0.75rem;
                font-size: 0.68rem;
                letter-spacing: 0.05em;
            }

            .nav-btn svg {
                display: none;
            }



            .main-headline {
                font-size: clamp(2.0rem, 8vw, 2.6rem);
            }

            .product-callouts {
                min-height: 250px;
            }

            .note-kiwi .cursive-text,
            .note-sugar .cursive-text {
                font-size: 0.98rem;
            }

            .cursive-arrow-svg {
                width: 36px;
                height: 30px;
            }

            .story-a-statements {
                min-height: 200px;
            }

            .story-a-statements .statement-item {
                padding: 0.95rem 1rem;
                gap: 0.75rem;
            }


        }
    </style>

    <!-- REWAVE Self-Contained Assets (Zero-CORS offline & file:/// execution) -->
    <script src="rewave_assets.js"></script>

    <!-- Standalone Three.js r160 + GLTFLoader + RoomEnvironment Bundle (Zero-CORS offline & file:/// execution) -->
    <script src="three_bundle.min.js"></script>
</head>

<body>

    <!-- Paper Grain Overlay -->
    <div class="paper-grain"></div>

    <!-- Unified Background Stage -->
    <div id="stage-bg"></div>

    <!-- 3D WebGL Canvas Layer -->
    <div id="webgl-container"></div>

    <!-- EDITORIAL OFF-CANVAS OVERLAY -->
    <div class="menu-overlay" id="menu-overlay" aria-hidden="true">
        <div class="overlay-backdrop" id="overlay-backdrop"></div>
        <div class="overlay-panel" id="overlay-panel" data-lenis-prevent>
            <div class="overlay-header">
                <div class="overlay-brand">
                    <svg class="overlay-logo-svg" viewBox="0 0 1162 200">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M 811.0 19.0 L 806.0 24.0 L 805.0 36.0 L 865.0 175.0 L 873.0 183.0 L 880.0 186.0 L 913.0 186.0 L 921.0 183.0 L 929.0 175.0 L 937.0 155.0 L 983.0 50.0 L 984.0 45.0 L 989.0 35.0 L 989.0 28.0 L 987.0 23.0 L 979.0 17.0 L 951.0 17.0 L 944.0 20.0 L 937.0 27.0 L 899.0 121.0 L 896.0 121.0 L 891.0 106.0 L 888.0 101.0 L 882.0 84.0 L 866.0 47.0 L 865.0 42.0 L 858.0 27.0 L 851.0 20.0 L 844.0 17.0 L 816.0 17.0 Z M 133.0 18.0 L 129.0 16.0 L 104.0 17.0 L 87.0 24.0 L 80.0 29.0 L 72.0 37.0 L 71.0 29.0 L 69.0 24.0 L 64.0 19.0 L 60.0 17.0 L 28.0 17.0 L 21.0 20.0 L 13.0 28.0 L 10.0 35.0 L 10.0 171.0 L 12.0 176.0 L 19.0 183.0 L 25.0 186.0 L 50.0 186.0 L 57.0 183.0 L 63.0 177.0 L 66.0 169.0 L 66.0 113.0 L 71.0 96.0 L 75.0 89.0 L 85.0 79.0 L 91.0 75.0 L 109.0 69.0 L 124.0 69.0 L 132.0 64.0 L 136.0 55.0 L 137.0 42.0 L 139.0 35.0 L 138.0 23.0 Z M 1058.0 15.0 L 1044.0 18.0 L 1027.0 25.0 L 1011.0 36.0 L 999.0 49.0 L 988.0 68.0 L 984.0 80.0 L 981.0 98.0 L 982.0 117.0 L 984.0 127.0 L 992.0 147.0 L 1002.0 161.0 L 1015.0 173.0 L 1030.0 182.0 L 1044.0 187.0 L 1059.0 190.0 L 1083.0 190.0 L 1104.0 185.0 L 1118.0 178.0 L 1125.0 173.0 L 1138.0 160.0 L 1142.0 154.0 L 1148.0 141.0 L 1147.0 134.0 L 1140.0 128.0 L 1108.0 128.0 L 1104.0 130.0 L 1090.0 144.0 L 1082.0 147.0 L 1067.0 148.0 L 1056.0 145.0 L 1048.0 141.0 L 1039.0 132.0 L 1034.0 122.0 L 1033.0 117.0 L 1034.0 113.0 L 1140.0 113.0 L 1145.0 111.0 L 1149.0 107.0 L 1152.0 101.0 L 1152.0 82.0 L 1149.0 68.0 L 1142.0 52.0 L 1133.0 40.0 L 1120.0 29.0 L 1108.0 22.0 L 1094.0 17.0 L 1083.0 15.0 Z M 1034.0 81.0 L 1037.0 73.0 L 1045.0 63.0 L 1057.0 56.0 L 1066.0 54.0 L 1079.0 55.0 L 1089.0 59.0 L 1097.0 66.0 L 1101.0 72.0 L 1103.0 78.0 L 1102.0 82.0 Z M 212.0 15.0 L 192.0 20.0 L 176.0 28.0 L 164.0 37.0 L 151.0 52.0 L 142.0 69.0 L 138.0 81.0 L 136.0 92.0 L 137.0 122.0 L 140.0 133.0 L 148.0 150.0 L 156.0 161.0 L 169.0 173.0 L 182.0 181.0 L 194.0 186.0 L 212.0 190.0 L 238.0 190.0 L 249.0 188.0 L 261.0 184.0 L 271.0 179.0 L 281.0 172.0 L 290.0 163.0 L 298.0 152.0 L 303.0 141.0 L 303.0 136.0 L 301.0 132.0 L 295.0 128.0 L 263.0 128.0 L 259.0 130.0 L 248.0 142.0 L 240.0 146.0 L 231.0 148.0 L 221.0 148.0 L 210.0 145.0 L 201.0 140.0 L 192.0 130.0 L 188.0 120.0 L 187.0 114.0 L 296.0 113.0 L 300.0 111.0 L 306.0 104.0 L 307.0 101.0 L 307.0 83.0 L 304.0 69.0 L 297.0 53.0 L 289.0 42.0 L 277.0 31.0 L 262.0 22.0 L 244.0 16.0 L 227.0 14.0 Z M 189.0 78.0 L 193.0 70.0 L 203.0 60.0 L 215.0 55.0 L 227.0 54.0 L 239.0 57.0 L 246.0 61.0 L 254.0 70.0 L 257.0 76.0 L 257.0 82.0 L 189.0 81.0 Z M 808.0 176.0 L 809.0 168.0 L 809.0 98.0 L 807.0 78.0 L 802.0 61.0 L 795.0 48.0 L 780.0 32.0 L 763.0 21.0 L 741.0 13.0 L 723.0 10.0 L 694.0 10.0 L 670.0 15.0 L 646.0 26.0 L 632.0 36.0 L 619.0 49.0 L 600.0 75.0 L 584.0 102.0 L 577.0 109.0 L 571.0 112.0 L 561.0 111.0 L 551.0 102.0 L 531.0 65.0 L 521.0 50.0 L 509.0 37.0 L 502.0 32.0 L 491.0 27.0 L 473.0 26.0 L 465.0 28.0 L 453.0 35.0 L 436.0 54.0 L 424.0 75.0 L 412.0 100.0 L 408.0 106.0 L 400.0 112.0 L 390.0 111.0 L 384.0 105.0 L 381.0 100.0 L 372.0 77.0 L 361.0 35.0 L 353.0 25.0 L 343.0 21.0 L 324.0 21.0 L 316.0 24.0 L 312.0 28.0 L 309.0 34.0 L 309.0 43.0 L 319.0 81.0 L 331.0 119.0 L 339.0 139.0 L 346.0 153.0 L 354.0 165.0 L 366.0 177.0 L 383.0 185.0 L 404.0 186.0 L 416.0 182.0 L 425.0 176.0 L 433.0 168.0 L 441.0 157.0 L 466.0 107.0 L 475.0 98.0 L 483.0 98.0 L 492.0 106.0 L 516.0 152.0 L 527.0 167.0 L 533.0 173.0 L 541.0 179.0 L 549.0 183.0 L 560.0 186.0 L 575.0 186.0 L 586.0 183.0 L 593.0 180.0 L 600.0 175.0 L 612.0 163.0 L 622.0 148.0 L 648.0 97.0 L 658.0 83.0 L 670.0 71.0 L 682.0 63.0 L 695.0 58.0 L 706.0 56.0 L 722.0 57.0 L 732.0 60.0 L 741.0 65.0 L 750.0 74.0 L 752.0 79.0 L 750.0 81.0 L 747.0 81.0 L 735.0 78.0 L 711.0 78.0 L 696.0 81.0 L 680.0 87.0 L 672.0 92.0 L 661.0 102.0 L 652.0 117.0 L 649.0 128.0 L 649.0 147.0 L 655.0 163.0 L 661.0 171.0 L 670.0 179.0 L 681.0 185.0 L 700.0 190.0 L 718.0 190.0 L 734.0 186.0 L 748.0 178.0 L 759.0 167.0 L 760.0 176.0 L 762.0 180.0 L 766.0 184.0 L 771.0 186.0 L 797.0 186.0 L 803.0 183.0 Z M 701.0 125.0 L 709.0 117.0 L 721.0 113.0 L 757.0 114.0 L 757.0 125.0 L 751.0 138.0 L 741.0 147.0 L 731.0 151.0 L 719.0 152.0 L 707.0 148.0 L 701.0 142.0 L 699.0 138.0 L 699.0 130.0 Z" />
                    </svg>
                </div>
                <button class="overlay-close-btn" id="menu-close" aria-label="Close Navigation Menu">
                    <span class="kinetic-text" data-text="CLOSE">CLOSE</span>
                    <span class="close-icon-circle">
                        <svg viewBox="0 0 20 20" fill="none">
                            <line x1="5" y1="5" x2="15" y2="15" stroke="currentColor" stroke-width="1.8"
                                stroke-linecap="round" />
                            <line x1="15" y1="5" x2="5" y2="15" stroke="currentColor" stroke-width="1.8"
                                stroke-linecap="round" />
                        </svg>
                    </span>
                </button>
            </div>

            <div class="overlay-body">
                <div class="overlay-nav">
                    <ul class="overlay-menu-list">
                        <li class="menu-item" data-preview="matrix">
                            <a href="#matrix" class="menu-link">
                                <span class="menu-num">01</span>
                                <span class="menu-title">BOTANICAL MATRIX</span>
                                <span class="menu-arrow-icon">
                                    <svg viewBox="0 0 24 24" fill="none">
                                        <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                            </a>
                        </li>
                        <li class="menu-item" data-preview="release">
                            <a href="#release" class="menu-link">
                                <span class="menu-num">02</span>
                                <span class="menu-title">THE RELEASE</span>
                                <span class="menu-arrow-icon">
                                    <svg viewBox="0 0 24 24" fill="none">
                                        <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                            </a>
                        </li>
                        <li class="menu-item" data-preview="rituals">
                            <a href="#rituals" class="menu-link">
                                <span class="menu-num">03</span>
                                <span class="menu-title">EVERYDAY RHYTHM</span>
                                <span class="menu-arrow-icon">
                                    <svg viewBox="0 0 24 24" fill="none">
                                        <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                            </a>
                        </li>
                        <li class="menu-item" data-preview="nutrition">
                            <a href="#matrix" class="menu-link">
                                <span class="menu-num">04</span>
                                <span class="menu-title">NUTRITIONAL SCIENCE</span>
                                <span class="menu-arrow-icon">
                                    <svg viewBox="0 0 24 24" fill="none">
                                        <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                            </a>
                        </li>
                        <li class="menu-item" data-preview="philosophy">
                            <a href="#footer" class="menu-link">
                                <span class="menu-num">05</span>
                                <span class="menu-title">BRAND PHILOSOPHY</span>
                                <span class="menu-arrow-icon">
                                    <svg viewBox="0 0 24 24" fill="none">
                                        <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </span>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="overlay-footer">
                <div class="overlay-footer-col">
                    <span class="footer-label">CARE & INQUIRIES</span>
                    <a href="mailto:care@rewave.in" class="footer-email">
                        care@rewave.in
                    </a>
                </div>
                <div class="overlay-footer-col">
                    <span class="footer-label">SOCIAL CULTURE</span>
                    <div class="overlay-socials">
                        <a href="https://instagram.com" target="_blank" rel="noopener"
                            style="color: var(--warm-bone); text-decoration: none;">Instagram</a>
                        <span class="separator">/</span>
                        <a href="https://tiktok.com" target="_blank" rel="noopener"
                            style="color: var(--warm-bone); text-decoration: none;">TikTok</a>
                        <span class="separator">/</span>
                        <a href="https://youtube.com" target="_blank" rel="noopener"
                            style="color: var(--warm-bone); text-decoration: none;">YouTube</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Floating Minimal Navigation with Left Hamburger, Center Docking Logo & Retouched SVG Buttons -->
    <nav class="nav-ui" id="main-nav">
        <div class="nav-left">
            <button class="nav-btn menu-btn" id="menu-toggle" aria-label="Open Navigation Menu" aria-expanded="false">
                <span class="btn-icon hamburger-icon">
                    <svg viewBox="0 0 20 20" fill="none">
                        <line class="line line-1" x1="3" y1="6" x2="17" y2="6" stroke="currentColor" stroke-width="1.8"
                            stroke-linecap="round" />
                        <line class="line line-2" x1="3" y1="10" x2="13" y2="10" stroke="currentColor"
                            stroke-width="1.8" stroke-linecap="round" />
                        <line class="line line-3" x1="3" y1="14" x2="17" y2="14" stroke="currentColor"
                            stroke-width="1.8" stroke-linecap="round" />
                    </svg>
                </span>
                <span class="kinetic-text" data-text="MENU">MENU</span>
            </button>

            <div class="nav-socials">
                <a href="https://instagram.com" target="_blank" rel="noopener" class="social-link" title="Instagram"
                    aria-label="Instagram">
                    <svg viewBox="0 0 24 24">
                        <path
                            d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
                    </svg>
                </a>
                <a href="https://tiktok.com" target="_blank" rel="noopener" class="social-link" title="TikTok"
                    aria-label="TikTok">
                    <svg viewBox="0 0 24 24">
                        <path
                            d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.24 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z" />
                    </svg>
                </a>
                <a href="https://youtube.com" target="_blank" rel="noopener" class="social-link" title="YouTube"
                    aria-label="YouTube">
                    <svg viewBox="0 0 24 24">
                        <path
                            d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z" />
                    </svg>
                </a>
            </div>
        </div>

        <!-- Center: Single Persistent Vector REWAVE Logo (Slides up & docks in header on scroll) -->
        <div class="nav-center-brand" id="nav-center-brand">
            <a href="#" class="nav-brand-link" aria-label="REWAVE Home">
                <svg class="main-brand-logo-svg" id="main-brand-logo" viewBox="0 0 1162 200">
                    <path fill-rule="evenodd" clip-rule="evenodd"
                        d="M 811.0 19.0 L 806.0 24.0 L 805.0 36.0 L 865.0 175.0 L 873.0 183.0 L 880.0 186.0 L 913.0 186.0 L 921.0 183.0 L 929.0 175.0 L 937.0 155.0 L 983.0 50.0 L 984.0 45.0 L 989.0 35.0 L 989.0 28.0 L 987.0 23.0 L 979.0 17.0 L 951.0 17.0 L 944.0 20.0 L 937.0 27.0 L 899.0 121.0 L 896.0 121.0 L 891.0 106.0 L 888.0 101.0 L 882.0 84.0 L 866.0 47.0 L 865.0 42.0 L 858.0 27.0 L 851.0 20.0 L 844.0 17.0 L 816.0 17.0 Z M 133.0 18.0 L 129.0 16.0 L 104.0 17.0 L 87.0 24.0 L 80.0 29.0 L 72.0 37.0 L 71.0 29.0 L 69.0 24.0 L 64.0 19.0 L 60.0 17.0 L 28.0 17.0 L 21.0 20.0 L 13.0 28.0 L 10.0 35.0 L 10.0 171.0 L 12.0 176.0 L 19.0 183.0 L 25.0 186.0 L 50.0 186.0 L 57.0 183.0 L 63.0 177.0 L 66.0 169.0 L 66.0 113.0 L 71.0 96.0 L 75.0 89.0 L 85.0 79.0 L 91.0 75.0 L 109.0 69.0 L 124.0 69.0 L 132.0 64.0 L 136.0 55.0 L 137.0 42.0 L 139.0 35.0 L 138.0 23.0 Z M 1058.0 15.0 L 1044.0 18.0 L 1027.0 25.0 L 1011.0 36.0 L 999.0 49.0 L 988.0 68.0 L 984.0 80.0 L 981.0 98.0 L 982.0 117.0 L 984.0 127.0 L 992.0 147.0 L 1002.0 161.0 L 1015.0 173.0 L 1030.0 182.0 L 1044.0 187.0 L 1059.0 190.0 L 1083.0 190.0 L 1104.0 185.0 L 1118.0 178.0 L 1125.0 173.0 L 1138.0 160.0 L 1142.0 154.0 L 1148.0 141.0 L 1147.0 134.0 L 1140.0 128.0 L 1108.0 128.0 L 1104.0 130.0 L 1090.0 144.0 L 1082.0 147.0 L 1067.0 148.0 L 1056.0 145.0 L 1048.0 141.0 L 1039.0 132.0 L 1034.0 122.0 L 1033.0 117.0 L 1034.0 113.0 L 1140.0 113.0 L 1145.0 111.0 L 1149.0 107.0 L 1152.0 101.0 L 1152.0 82.0 L 1149.0 68.0 L 1142.0 52.0 L 1133.0 40.0 L 1120.0 29.0 L 1108.0 22.0 L 1094.0 17.0 L 1083.0 15.0 Z M 1034.0 81.0 L 1037.0 73.0 L 1045.0 63.0 L 1057.0 56.0 L 1066.0 54.0 L 1079.0 55.0 L 1089.0 59.0 L 1097.0 66.0 L 1101.0 72.0 L 1103.0 78.0 L 1102.0 82.0 Z M 212.0 15.0 L 192.0 20.0 L 176.0 28.0 L 164.0 37.0 L 151.0 52.0 L 142.0 69.0 L 138.0 81.0 L 136.0 92.0 L 137.0 122.0 L 140.0 133.0 L 148.0 150.0 L 156.0 161.0 L 169.0 173.0 L 182.0 181.0 L 194.0 186.0 L 212.0 190.0 L 238.0 190.0 L 249.0 188.0 L 261.0 184.0 L 271.0 179.0 L 281.0 172.0 L 290.0 163.0 L 298.0 152.0 L 303.0 141.0 L 303.0 136.0 L 301.0 132.0 L 295.0 128.0 L 263.0 128.0 L 259.0 130.0 L 248.0 142.0 L 240.0 146.0 L 231.0 148.0 L 221.0 148.0 L 210.0 145.0 L 201.0 140.0 L 192.0 130.0 L 188.0 120.0 L 187.0 114.0 L 296.0 113.0 L 300.0 111.0 L 306.0 104.0 L 307.0 101.0 L 307.0 83.0 L 304.0 69.0 L 297.0 53.0 L 289.0 42.0 L 277.0 31.0 L 262.0 22.0 L 244.0 16.0 L 227.0 14.0 Z M 189.0 78.0 L 193.0 70.0 L 203.0 60.0 L 215.0 55.0 L 227.0 54.0 L 239.0 57.0 L 246.0 61.0 L 254.0 70.0 L 257.0 76.0 L 257.0 82.0 L 189.0 81.0 Z M 808.0 176.0 L 809.0 168.0 L 809.0 98.0 L 807.0 78.0 L 802.0 61.0 L 795.0 48.0 L 780.0 32.0 L 763.0 21.0 L 741.0 13.0 L 723.0 10.0 L 694.0 10.0 L 670.0 15.0 L 646.0 26.0 L 632.0 36.0 L 619.0 49.0 L 600.0 75.0 L 584.0 102.0 L 577.0 109.0 L 571.0 112.0 L 561.0 111.0 L 551.0 102.0 L 531.0 65.0 L 521.0 50.0 L 509.0 37.0 L 502.0 32.0 L 491.0 27.0 L 473.0 26.0 L 465.0 28.0 L 453.0 35.0 L 436.0 54.0 L 424.0 75.0 L 412.0 100.0 L 408.0 106.0 L 400.0 112.0 L 390.0 111.0 L 384.0 105.0 L 381.0 100.0 L 372.0 77.0 L 361.0 35.0 L 353.0 25.0 L 343.0 21.0 L 324.0 21.0 L 316.0 24.0 L 312.0 28.0 L 309.0 34.0 L 309.0 43.0 L 319.0 81.0 L 331.0 119.0 L 339.0 139.0 L 346.0 153.0 L 354.0 165.0 L 366.0 177.0 L 383.0 185.0 L 404.0 186.0 L 416.0 182.0 L 425.0 176.0 L 433.0 168.0 L 441.0 157.0 L 466.0 107.0 L 475.0 98.0 L 483.0 98.0 L 492.0 106.0 L 516.0 152.0 L 527.0 167.0 L 533.0 173.0 L 541.0 179.0 L 549.0 183.0 L 560.0 186.0 L 575.0 186.0 L 586.0 183.0 L 593.0 180.0 L 600.0 175.0 L 612.0 163.0 L 622.0 148.0 L 648.0 97.0 L 658.0 83.0 L 670.0 71.0 L 682.0 63.0 L 695.0 58.0 L 706.0 56.0 L 722.0 57.0 L 732.0 60.0 L 741.0 65.0 L 750.0 74.0 L 752.0 79.0 L 750.0 81.0 L 747.0 81.0 L 735.0 78.0 L 711.0 78.0 L 696.0 81.0 L 680.0 87.0 L 672.0 92.0 L 661.0 102.0 L 652.0 117.0 L 649.0 128.0 L 649.0 147.0 L 655.0 163.0 L 661.0 171.0 L 670.0 179.0 L 681.0 185.0 L 700.0 190.0 L 718.0 190.0 L 734.0 186.0 L 748.0 178.0 L 759.0 167.0 L 760.0 176.0 L 762.0 180.0 L 766.0 184.0 L 771.0 186.0 L 797.0 186.0 L 803.0 183.0 Z M 701.0 125.0 L 709.0 117.0 L 721.0 113.0 L 757.0 114.0 L 757.0 125.0 L 751.0 138.0 L 741.0 147.0 L 731.0 151.0 L 719.0 152.0 L 707.0 148.0 L 701.0 142.0 L 699.0 138.0 L 699.0 130.0 Z" />
                </svg>
            </a>
        </div>

        <div class="nav-right">
            <a href="#matrix" class="nav-btn shop-btn">
                <span class="kinetic-text" data-text="SHOP ALL">SHOP ALL</span>
                <span class="btn-arrow-circle">
                    <svg viewBox="0 0 20 20" fill="none">
                        <path d="M4.5 10H15.5M15.5 10L10.5 5M15.5 10L10.5 15" stroke="currentColor" stroke-width="1.8"
                            stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                </span>
            </a>
        </div>
    </nav>

    <!-- Main Landing Experience -->
    <main>
        <!-- HERO SECTION -->
        <section class="hero">
            <div class="hero-body">
                <!-- Left Side: Editorial Cursive Notes (Zero Clutter, Full Bottle Clearance) -->
                <div class="product-callouts">
                    <!-- Cursive Note 1: Upper-left, completely clear of bottle cap and wordmark -->
                    <div class="cursive-annotation note-kiwi">
                        <span class="cursive-text">Cold-Pressed Kiwi,<br>Crisp Hydration</span>
                        <svg class="cursive-arrow-svg" viewBox="0 0 65 55" fill="none">
                            <path d="M 12,8 C 18,28 32,44 54,46" stroke="var(--forest-green)" stroke-width="2.2"
                                stroke-linecap="round" />
                            <path d="M 44,40 L 55,46 L 47,53" stroke="var(--forest-green)" stroke-width="2.2"
                                stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>

                    <!-- Cursive Note 2: Mid-right, clear of bottle body, pointing left at label with ample breathing room -->
                    <div class="cursive-annotation note-sugar">
                        <svg class="cursive-arrow-svg" viewBox="0 0 65 55" fill="none">
                            <path d="M 50,44 C 38,24 24,16 12,14" stroke="var(--forest-green)" stroke-width="2.2"
                                stroke-linecap="round" />
                            <path d="M 22,8 L 10,14 L 18,22" stroke="var(--forest-green)" stroke-width="2.2"
                                stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                        <span class="cursive-text">100% Botanicals,<br>Original Taste</span>
                    </div>
                </div>

                <!-- Right Side: Headline Column in High-Contrast Deep Forest ink -->
                <div class="headline-column">
                    <div class="headline-tag">KIWI CUCUMBER · 250 ML FUNCTIONAL TONIC</div>
                    <h1 class="main-headline">
                        <span class="headline-row"><span class="headline-word color-forest">MATCH YOUR</span></span>
                        <span class="headline-row"><span class="headline-word color-forest">EVERYDAY</span></span>
                        <span class="headline-row"><span class="headline-word color-forest">RHYTHM<span
                                    class="headline-dot">.</span></span></span>
                    </h1>

                    <p class="hero-desc">
                        Wellness that moves with you. A refreshing approach to everyday functional nutrition, powered by
                        cold-pressed kiwi juice, cucumber extract, and active prebiotic fibre.
                    </p>

                    <div class="cta-group">
                        <a href="#matrix" class="hero-cta">
                            <span class="kinetic-text" data-text="EXPLORE REWAVE">EXPLORE REWAVE</span>
                            <span class="cta-arrow-circle">
                                <svg viewBox="0 0 20 20" fill="none">
                                    <path d="M4.5 10H15.5M15.5 10L10.5 5M15.5 10L10.5 15" stroke="currentColor"
                                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                </svg>
                            </span>
                        </a>
                        <a href="#rituals" class="hero-secondary-link">Daily Rituals</a>
                    </div>
                </div>
            </div>

            <!-- Refined Editorial Marquee Divider -->
            <div class="marquee-ribbon-wrap" id="marquee-ribbon">
                <div class="marquee-track">
                    <div class="marquee-item">
                        <span>RELEASE</span> <span class="marquee-dot"></span>
                        <span>RENEW</span> <span class="marquee-dot"></span>
                        <span>RECHARGE</span> <span class="marquee-dot"></span>
                        <span class="accent-word">100% BOTANICAL TONIC</span> <span class="marquee-dot"></span>
                        <span>COLD-PRESSED RAW</span> <span class="marquee-dot"></span>
                        <span>RELEASE</span> <span class="marquee-dot"></span>
                        <span>RENEW</span> <span class="marquee-dot"></span>
                        <span>RECHARGE</span> <span class="marquee-dot"></span>
                        <span class="accent-word">EVERYDAY RHYTHM</span> <span class="marquee-dot"></span>
                    </div>
                    <div class="marquee-item" aria-hidden="true">
                        <span>RELEASE</span> <span class="marquee-dot"></span>
                        <span>RENEW</span> <span class="marquee-dot"></span>
                        <span>RECHARGE</span> <span class="marquee-dot"></span>
                        <span class="accent-word">100% BOTANICAL TONIC</span> <span class="marquee-dot"></span>
                        <span>COLD-PRESSED RAW</span> <span class="marquee-dot"></span>
                        <span>RELEASE</span> <span class="marquee-dot"></span>
                        <span>RENEW</span> <span class="marquee-dot"></span>
                        <span>RECHARGE</span> <span class="marquee-dot"></span>
                        <span class="accent-word">EVERYDAY RHYTHM</span> <span class="marquee-dot"></span>
                    </div>
                </div>
            </div>
        </section>

        <!-- STORY A: "FUNCTIONAL BY DESIGN" PINNED STAGE -->
        <section class="story-a-section" id="matrix">
            <div class="story-a-container">
                <div class="story-a-content">
                    <div class="story-a-header">
                        <div class="section-tag">01 / The Botanical Matrix</div>
                        <h2 class="section-title">FUNCTIONAL BY DESIGN</h2>
                        <p class="section-intro">
                            Every sip of Kiwi Cucumber is formulated with precision. Pure cold-pressed botanicals meet
                            prebiotic gut-support for balanced, sustainable vitality.
                        </p>
                    </div>

                    <div class="story-a-statements">
                        <div class="statement-item active" id="stmt-1">
                            <span class="stmt-num">01</span>
                            <div class="stmt-content">
                                <h3 class="stmt-title">Prebiotic Fibre</h3>
                                <p class="stmt-desc">2.5g certified plant-based dietary fibre per bottle. Nourishes
                                    microbiome equilibrium and promotes steady digestive rhythm.</p>
                                <span class="stmt-badge">Microbiome Fuel · 2.5g Fibre</span>
                            </div>
                        </div>

                        <div class="statement-item dimmed" id="stmt-2">
                            <span class="stmt-num">02</span>
                            <div class="stmt-content">
                                <h3 class="stmt-title">Cold-Pressed Kiwi Juice</h3>
                                <p class="stmt-desc">Real whole fruit delivering crisp natural acidity, essential
                                    micronutrients, and vibrant organic flavour without artificial additives.</p>
                                <span class="stmt-badge">Whole Fruit Nutrition</span>
                            </div>
                        </div>

                        <div class="statement-item dimmed" id="stmt-3">
                            <span class="stmt-num">03</span>
                            <div class="stmt-content">
                                <h3 class="stmt-title">Crisp Cucumber Extract</h3>
                                <p class="stmt-desc">Hydro-cooling botanical extract formulated with pure water and
                                    natural essence for clean cellular hydration and effortless recovery.</p>
                                <span class="stmt-badge">Cellular Hydration</span>
                            </div>
                        </div>

                        <div class="statement-item dimmed" id="stmt-4">
                            <span class="stmt-num">04</span>
                            <div class="stmt-content">
                                <h3 class="stmt-title">Clean Caloric Balance</h3>
                                <p class="stmt-desc">Only 48 kcal and 7.8g natural fruit sugars per 250 ml. Zero added
                                    cane sugar, zero artificial sweeteners, zero synthetic preservatives.</p>
                                <span class="stmt-badge">48 kcal · 0g Fat · FSSAI</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Stage reserved for the 3D bottle in Story A -->
                <div class="story-a-bottle-stage"></div>
            </div>
        </section>

        <!-- STORY B: "RELEASE" DECONSTRUCTED ARCHITECTURE PINNED STAGE -->
        <section class="story-b-section" id="release">
            <div class="story-b-grid-wrap">
                <!-- Top Header: Eyebrow + Monolithic Headline -->
                <header class="story-b-header">
                    <div class="story-b-meta-bar">
                        <div class="section-tag story-b-tag">
                            <span class="section-tag-dot"></span>
                            <span>02 // FORMULATION ARCHITECTURE</span>
                        </div>
                        <span class="meta-coords">SPEC: REWAVE-KC250 // DECONSTRUCTED MATRIX</span>
                    </div>
                    <h2 class="story-b-headline">
                        <span class="story-b-title-main">RELEASE.</span>
                        <span class="story-b-title-accent" id="story-b-accent">THE RAW MATRIX.</span>
                    </h2>
                </header>

                <!-- Deconstructed Botanical Hotspots Surrounding Center 3D Bottle -->
                <div class="story-b-architecture">
                    <!-- Left Column: Node 01 (Cap) and Node 03 (Prebiotic) -->
                    <div class="deconstruct-col deconstruct-left">
                        <div class="deconstruct-node" id="node-cap" data-component="cap">
                            <div class="node-meta">
                                <span class="node-index">01</span>
                                <span class="node-system">CLOSURE // VOLATILE LOCK</span>
                            </div>
                            <h3 class="node-title">Precision Oxygen Barrier Cap</h3>
                            <p class="node-desc">Custom high-density seal preserving cold-pressed volatile aromatics,
                                live active enzymes, and natural effervescence without oxidation.</p>
                            <div class="node-tags">
                                <span class="node-tag">100% HDPE</span>
                                <span class="node-tag">Hermetic Seal</span>
                            </div>
                            <div class="node-pointer pointer-right">
                                <div class="pointer-line"></div>
                                <div class="pointer-dot"></div>
                            </div>
                        </div>

                        <div class="deconstruct-node" id="node-prebiotic" data-component="prebiotic">
                            <div class="node-meta">
                                <span class="node-index">03</span>
                                <span class="node-system">BIO-ACTIVES // GUT EQUILIBRIUM</span>
                            </div>
                            <h3 class="node-title">2.5g Active Prebiotic Plant Fibre</h3>
                            <p class="node-desc">Calibrated plant-derived soluble fibre nourishing diverse gut
                                microbiome flora for steady, sustained metabolic release.</p>
                            <div class="node-tags">
                                <span class="node-tag">2.5g Fibre</span>
                                <span class="node-tag">Microbiome Fuel</span>
                            </div>
                            <div class="node-pointer pointer-right">
                                <div class="pointer-line"></div>
                                <div class="pointer-dot"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Center zone: Reserved exclusively for 3D bottle and elevated floating cap -->
                    <div class="deconstruct-center-void" aria-hidden="true"></div>

                    <!-- Right Column: Node 02 (Kiwi) and Node 04 (Cucumber) -->
                    <div class="deconstruct-col deconstruct-right">
                        <div class="deconstruct-node" id="node-kiwi" data-component="kiwi">
                            <div class="node-meta">
                                <span class="node-index">02</span>
                                <span class="node-system">EXTRACT // ENZYMATIC VITALITY</span>
                            </div>
                            <h3 class="node-title">Raw Cold-Pressed Kiwi Juice</h3>
                            <p class="node-desc">Real whole fruit extracted under zero-thermal pressure. Delivers
                                organic vitamin C, bioavailable polyphenols, and crisp natural acidity.</p>
                            <div class="node-tags">
                                <span class="node-tag">Cold-Pressed Raw</span>
                                <span class="node-tag">Zero Heat</span>
                            </div>
                            <div class="node-pointer pointer-left">
                                <div class="pointer-dot"></div>
                                <div class="pointer-line"></div>
                            </div>
                        </div>

                        <div class="deconstruct-node" id="node-hydro" data-component="hydro">
                            <div class="node-meta">
                                <span class="node-index">04</span>
                                <span class="node-system">HYDRATION // OSMOLYTE RECOVERY</span>
                            </div>
                            <h3 class="node-title">Hydro-Cooling Cucumber Matrix</h3>
                            <p class="node-desc">Clean cellular hydration infused with crisp botanical cucumber essence.
                                Only 48 kcal per bottle with zero refined cane sugar.</p>
                            <div class="node-tags">
                                <span class="node-tag">48 Kcal</span>
                                <span class="node-tag">FSSAI Certified</span>
                            </div>
                            <div class="node-pointer pointer-left">
                                <div class="pointer-dot"></div>
                                <div class="pointer-line"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Bottom Edge: Hairline-Separated Spec Strip -->
                <footer class="story-b-spec-strip" id="story-b-specs">
                    <div class="spec-item">
                        <span class="spec-text">250 ML NET</span>
                    </div>
                    <span class="spec-dot" aria-hidden="true"></span>
                    <div class="spec-item">
                        <span class="spec-text">48 KCAL ENERGY</span>
                    </div>
                    <span class="spec-dot" aria-hidden="true"></span>
                    <div class="spec-item">
                        <span class="spec-text">2.5 G PREBIOTIC FIBRE</span>
                    </div>
                    <span class="spec-dot" aria-hidden="true"></span>
                    <div class="spec-item">
                        <span class="spec-text">100% RECYCLABLE HDPE</span>
                    </div>
                    <span class="spec-dot" aria-hidden="true"></span>
                    <div class="spec-item">
                        <span class="spec-text">FSSAI LICENSED</span>
                    </div>
                </footer>
            </div>
        </section>

        <!-- DAILY RITUALS SECTION -->
        <section class="rituals-section" id="rituals">
            <div class="rituals-container">
                <div class="rituals-header">
                    <div class="section-tag" style="color: var(--lime-accent);">
                        <span class="section-tag-dot"></span>
                        <span>03 / Everyday Rhythm</span>
                    </div>
                    <h2 class="rituals-title">DESIGNED FOR YOUR DAY</h2>
                </div>

                <div class="rituals-grid">
                    <!-- Ritual 01: Morning Spark -->
                    <div class="ritual-item">
                        <div class="ritual-img-wrap">
                            <img src="assets/ritual_leaf_drops.jpg" alt="Cold-pressed botanical dew and hydration"
                                class="ritual-img" loading="lazy">
                            <div class="ritual-badge">08:00 AM</div>
                            <div class="ritual-img-overlay-tag"><em>the</em> morning awakening</div>
                        </div>
                        <div class="ritual-content">
                            <div class="ritual-time">
                                <span>MORNING SPARK</span>
                                <span class="spec-dot" style="margin: 0 0.4rem;"></span>
                                <span>HYDRATION</span>
                            </div>
                            <h3 class="ritual-heading">HYDRATE & AWAKEN</h3>
                            <p class="ritual-text">Start clean. Before coffee or after morning movement, replenish
                                minerals and essential hydration with crisp cold-pressed kiwi notes.</p>
                        </div>
                    </div>

                    <!-- Ritual 02: Afternoon Reset -->
                    <div class="ritual-item">
                        <div class="ritual-img-wrap">
                            <img src="assets/ritual_hands_botanical.jpg" alt="Botanical herbs and natural equilibrium"
                                class="ritual-img" loading="lazy">
                            <div class="ritual-badge">02:30 PM</div>
                            <div class="ritual-img-overlay-tag"><em>the</em> science of balance</div>
                        </div>
                        <div class="ritual-content">
                            <div class="ritual-time">
                                <span>AFTERNOON RESET</span>
                                <span class="spec-dot" style="margin: 0 0.4rem;"></span>
                                <span>MOMENTUM</span>
                            </div>
                            <h3 class="ritual-heading">SUSTAIN MOMENTUM</h3>
                            <p class="ritual-text">Smooth, sustained vitality without caffeine spikes or afternoon
                                crashes. Supports digestion and keeps your daily focus effortless.</p>
                        </div>
                    </div>

                    <!-- Ritual 03: Evening Restore -->
                    <div class="ritual-item">
                        <div class="ritual-img-wrap">
                            <img src="assets/ritual_sun_skin.jpg" alt="Sun-dappled skin and evening calm energy"
                                class="ritual-img" loading="lazy">
                            <div class="ritual-badge">08:00 PM</div>
                            <div class="ritual-img-overlay-tag"><em>the</em> calm energy</div>
                        </div>
                        <div class="ritual-content">
                            <div class="ritual-time">
                                <span>EVENING RESTORE</span>
                                <span class="spec-dot" style="margin: 0 0.4rem;"></span>
                                <span>UNWIND</span>
                            </div>
                            <h3 class="ritual-heading">RESTORE & SETTLE</h3>
                            <p class="ritual-text">Pairs effortlessly with meals or serves as a mindful botanical
                                aperitif to support microbiome equilibrium and restorative rest.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- NUTRITIONAL TRANSPARENCY: "READ THE LABEL" -->
        <section class="transparency-section" id="transparency">
            <div class="transparency-container">
                <div class="transparency-left">
                    <div class="section-tag" style="color: var(--lime-accent);">
                        <span class="section-tag-dot"></span>
                        <span>04 / Formulation Facts</span>
                    </div>
                    <h2 class="transparency-title">SCIENCE IN PLAIN SIGHT.</h2>
                    <p class="transparency-desc">
                        No proprietary blends or hidden sugars. Every single ingredient in REWAVE is verified,
                        purposeful, and calibrated to support your daily metabolic and microbiome rhythm.
                    </p>
                    <div class="fssai-verification-badge">
                        <div class="fssai-mark">FSSAI</div>
                        <div class="fssai-details">
                            <span class="fssai-lbl">CERTIFIED FUNCTIONAL BEVERAGE</span>
                            <span class="fssai-lic">LIC. NO. 10023022001890 [VERIFY WITH CLIENT]</span>
                        </div>
                    </div>
                </div>

                <div class="transparency-right">
                    <div class="nutrition-card">
                        <div class="nutrition-card-header">
                            <span class="card-title">NUTRITION INFORMATION</span>
                            <span class="card-serve">PER 250 ML BOTTLE</span>
                        </div>
                        <div class="nutrition-table">
                            <div class="nutri-row">
                                <span class="nutri-name">Energy</span>
                                <span class="nutri-val highlight-val">48 kcal</span>
                            </div>
                            <div class="nutri-row">
                                <span class="nutri-name">Dietary Fibre (Prebiotic)</span>
                                <span class="nutri-val highlight-val">2.5 g</span>
                            </div>
                            <div class="nutri-row">
                                <span class="nutri-name">Total Carbohydrates</span>
                                <span class="nutri-val">11.2 g</span>
                            </div>
                            <div class="nutri-row sub-row">
                                <span class="nutri-name">Total Sugars (Fruit-Derived)</span>
                                <span class="nutri-val">7.8 g</span>
                            </div>
                            <div class="nutri-row sub-row">
                                <span class="nutri-name">Added Sugars</span>
                                <span class="nutri-val">0.0 g</span>
                            </div>
                            <div class="nutri-row">
                                <span class="nutri-name">Protein</span>
                                <span class="nutri-val">0.2 g</span>
                            </div>
                            <div class="nutri-row">
                                <span class="nutri-name">Total Fat</span>
                                <span class="nutri-val">0.0 g</span>
                            </div>
                        </div>
                        <div class="nutrition-card-footer">
                            <div class="ingredients-header">INGREDIENTS:</div>
                            <p class="ingredients-list">
                                Filtered Water, Cold-Pressed Kiwi Juice, Cucumber Extract, Prebiotic Acacia Fibre,
                                Natural Botanical Flavours.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- EDITORIAL BRAND FOOTER -->
        <footer id="footer" class="site-footer">
            <!-- Full Width Landscape Artwork -->
            <div class="footer-landscape-container">
                <picture class="footer-landscape-picture">
                    <source media="(max-width: 768px)" srcset="assets/img/footer-landscape-mobile.webp" width="940" height="724">
                    <img src="assets/img/footer-landscape.webp" alt="" aria-hidden="true" width="2172" height="724" loading="lazy" class="footer-landscape-img">
                </picture>
            </div>

            <!-- Content Area Pulled Up Into Solid Dark Base -->
            <div class="footer-content">
                <!-- Headline with Overflow Masks for Slide-Up Motion -->
                <div class="footer-headline-wrap">
                    <h2 class="footer-headline">
                        <span class="footer-headline-mask">
                            <span class="footer-headline-line footer-headline-anton">Modern wellness,</span>
                        </span>
                        <span class="footer-headline-mask">
                            <span class="footer-headline-line footer-headline-serif">made enjoyable.</span>
                        </span>
                    </h2>
                </div>

                <!-- Main Navigation & Newsletter Row -->
                <div class="footer-main-row">
                    <!-- Column 1: Logo + Copyright -->
                    <div class="footer-col footer-col-brand">
                        <svg class="footer-logo-svg" viewBox="0 0 1162 200" aria-label="REWAVE">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M 811.0 19.0 L 806.0 24.0 L 805.0 36.0 L 865.0 175.0 L 873.0 183.0 L 880.0 186.0 L 913.0 186.0 L 921.0 183.0 L 929.0 175.0 L 937.0 155.0 L 983.0 50.0 L 984.0 45.0 L 989.0 35.0 L 989.0 28.0 L 987.0 23.0 L 979.0 17.0 L 951.0 17.0 L 944.0 20.0 L 937.0 27.0 L 899.0 121.0 L 896.0 121.0 L 891.0 106.0 L 888.0 101.0 L 882.0 84.0 L 866.0 47.0 L 865.0 42.0 L 858.0 27.0 L 851.0 20.0 L 844.0 17.0 L 816.0 17.0 Z M 133.0 18.0 L 129.0 16.0 L 104.0 17.0 L 87.0 24.0 L 80.0 29.0 L 72.0 37.0 L 71.0 29.0 L 69.0 24.0 L 64.0 19.0 L 60.0 17.0 L 28.0 17.0 L 21.0 20.0 L 13.0 28.0 L 10.0 35.0 L 10.0 171.0 L 12.0 176.0 L 19.0 183.0 L 25.0 186.0 L 50.0 186.0 L 57.0 183.0 L 63.0 177.0 L 66.0 169.0 L 66.0 113.0 L 71.0 96.0 L 75.0 89.0 L 85.0 79.0 L 91.0 75.0 L 109.0 69.0 L 124.0 69.0 L 132.0 64.0 L 136.0 55.0 L 137.0 42.0 L 139.0 35.0 L 138.0 23.0 Z M 1058.0 15.0 L 1044.0 18.0 L 1027.0 25.0 L 1011.0 36.0 L 999.0 49.0 L 988.0 68.0 L 984.0 80.0 L 981.0 98.0 L 982.0 117.0 L 984.0 127.0 L 992.0 147.0 L 1002.0 161.0 L 1015.0 173.0 L 1030.0 182.0 L 1044.0 187.0 L 1059.0 190.0 L 1083.0 190.0 L 1104.0 185.0 L 1118.0 178.0 L 1125.0 173.0 L 1138.0 160.0 L 1142.0 154.0 L 1148.0 141.0 L 1147.0 134.0 L 1140.0 128.0 L 1108.0 128.0 L 1104.0 130.0 L 1090.0 144.0 L 1082.0 147.0 L 1067.0 148.0 L 1056.0 145.0 L 1048.0 141.0 L 1039.0 132.0 L 1034.0 122.0 L 1033.0 117.0 L 1034.0 113.0 L 1140.0 113.0 L 1145.0 111.0 L 1149.0 107.0 L 1152.0 101.0 L 1152.0 82.0 L 1149.0 68.0 L 1142.0 52.0 L 1133.0 40.0 L 1120.0 29.0 L 1108.0 22.0 L 1094.0 17.0 L 1083.0 15.0 Z M 1034.0 81.0 L 1037.0 73.0 L 1045.0 63.0 L 1057.0 56.0 L 1066.0 54.0 L 1079.0 55.0 L 1089.0 59.0 L 1097.0 66.0 L 1101.0 72.0 L 1103.0 78.0 L 1102.0 82.0 Z M 212.0 15.0 L 192.0 20.0 L 176.0 28.0 L 164.0 37.0 L 151.0 52.0 L 142.0 69.0 L 138.0 81.0 L 136.0 92.0 L 137.0 122.0 L 140.0 133.0 L 148.0 150.0 L 156.0 161.0 L 169.0 173.0 L 182.0 181.0 L 194.0 186.0 L 212.0 190.0 L 238.0 190.0 L 249.0 188.0 L 261.0 184.0 L 271.0 179.0 L 281.0 172.0 L 290.0 163.0 L 298.0 152.0 L 303.0 141.0 L 303.0 136.0 L 301.0 132.0 L 295.0 128.0 L 263.0 128.0 L 259.0 130.0 L 248.0 142.0 L 240.0 146.0 L 231.0 148.0 L 221.0 148.0 L 210.0 145.0 L 201.0 140.0 L 192.0 130.0 L 188.0 120.0 L 187.0 114.0 L 296.0 113.0 L 300.0 111.0 L 306.0 104.0 L 307.0 101.0 L 307.0 83.0 L 304.0 69.0 L 297.0 53.0 L 289.0 42.0 L 277.0 31.0 L 262.0 22.0 L 244.0 16.0 L 227.0 14.0 Z M 189.0 78.0 L 193.0 70.0 L 203.0 60.0 L 215.0 55.0 L 227.0 54.0 L 239.0 57.0 L 246.0 61.0 L 254.0 70.0 L 257.0 76.0 L 257.0 82.0 L 189.0 81.0 Z M 808.0 176.0 L 809.0 168.0 L 809.0 98.0 L 807.0 78.0 L 802.0 61.0 L 795.0 48.0 L 780.0 32.0 L 763.0 21.0 L 741.0 13.0 L 723.0 10.0 L 694.0 10.0 L 670.0 15.0 L 646.0 26.0 L 632.0 36.0 L 619.0 49.0 L 600.0 75.0 L 584.0 102.0 L 577.0 109.0 L 571.0 112.0 L 561.0 111.0 L 551.0 102.0 L 531.0 65.0 L 521.0 50.0 L 509.0 37.0 L 502.0 32.0 L 491.0 27.0 L 473.0 26.0 L 465.0 28.0 L 453.0 35.0 L 436.0 54.0 L 424.0 75.0 L 412.0 100.0 L 408.0 106.0 L 400.0 112.0 L 390.0 111.0 L 384.0 105.0 L 381.0 100.0 L 372.0 77.0 L 361.0 35.0 L 353.0 25.0 L 343.0 21.0 L 324.0 21.0 L 316.0 24.0 L 312.0 28.0 L 309.0 34.0 L 309.0 43.0 L 319.0 81.0 L 331.0 119.0 L 339.0 139.0 L 346.0 153.0 L 354.0 165.0 L 366.0 177.0 L 383.0 185.0 L 404.0 186.0 L 416.0 182.0 L 425.0 176.0 L 433.0 168.0 L 441.0 157.0 L 466.0 107.0 L 475.0 98.0 L 483.0 98.0 L 492.0 106.0 L 516.0 152.0 L 527.0 167.0 L 533.0 173.0 L 541.0 179.0 L 549.0 183.0 L 560.0 186.0 L 575.0 186.0 L 586.0 183.0 L 593.0 180.0 L 600.0 175.0 L 612.0 163.0 L 622.0 148.0 L 648.0 97.0 L 658.0 83.0 L 670.0 71.0 L 682.0 63.0 L 695.0 58.0 L 706.0 56.0 L 722.0 57.0 L 732.0 60.0 L 741.0 65.0 L 750.0 74.0 L 752.0 79.0 L 750.0 81.0 L 747.0 81.0 L 735.0 78.0 L 711.0 78.0 L 696.0 81.0 L 680.0 87.0 L 672.0 92.0 L 661.0 102.0 L 652.0 117.0 L 649.0 128.0 L 649.0 147.0 L 655.0 163.0 L 661.0 171.0 L 670.0 179.0 L 681.0 185.0 L 700.0 190.0 L 718.0 190.0 L 734.0 186.0 L 748.0 178.0 L 759.0 167.0 L 760.0 176.0 L 762.0 180.0 L 766.0 184.0 L 771.0 186.0 L 797.0 186.0 L 803.0 183.0 Z M 701.0 125.0 L 709.0 117.0 L 721.0 113.0 L 757.0 114.0 L 757.0 125.0 L 751.0 138.0 L 741.0 147.0 L 731.0 151.0 L 719.0 152.0 L 707.0 148.0 L 701.0 142.0 L 699.0 138.0 L 699.0 130.0 Z" />
                        </svg>
                        <div class="footer-copy-text">© 2026 REWAVE</div>
                    </div>

                    <!-- Column 2 & 3 wrapper for mobile side-by-side pairing -->
                    <div class="footer-nav-pair">
                        <!-- Column 2: Explore -->
                        <div class="footer-col footer-col-nav">
                            <h3 class="footer-col-title">Explore</h3>
                            <ul class="footer-nav-list">
                                <li><a href="#matrix" class="footer-link">The Drink</a></li>
                                <li><a href="#transparency" class="footer-link">What's Inside</a></li>
                                <li><a href="#rituals" class="footer-link">Daily Rituals</a></li>
                            </ul>
                        </div>

                        <!-- Column 3: Follow -->
                        <div class="footer-col footer-col-nav">
                            <h3 class="footer-col-title">Follow</h3>
                            <ul class="footer-nav-list">
                                <li><a href="#" class="footer-link">Instagram</a></li>
                                <li><a href="#" class="footer-link">TikTok</a></li>
                                <li><a href="#" class="footer-link">YouTube</a></li>
                            </ul>
                        </div>
                    </div>

                    <!-- Column 4: Stay in the loop -->
                    <div class="footer-col footer-col-newsletter">
                        <h3 class="footer-col-title">Stay in the loop</h3>
                        <p class="footer-newsletter-text">Launching soon. Be the first to know.</p>
                        <form class="footer-form" id="footer-newsletter-form" novalidate>
                            <div class="footer-input-wrap">
                                <label for="footer-email-input" class="sr-only">Email address</label>
                                <input type="email" id="footer-email-input" class="footer-email-input" placeholder="Your email address" required autocomplete="email">
                                <button type="submit" class="footer-submit-btn">NOTIFY ME</button>
                            </div>
                            <div class="footer-form-feedback" id="footer-form-feedback" role="alert" aria-live="polite"></div>
                        </form>
                        <div class="footer-form-success" id="footer-form-success" style="display: none;" role="status" aria-live="polite">
                            Thank you. We'll be in touch.
                        </div>
                    </div>
                </div>

                <!-- Hairline Bottom Row -->
                <div class="footer-bottom-row">
                    <div class="footer-bottom-left">Science you can enjoy.</div>
                    <div class="footer-bottom-right">Release. Renew. Recharge.</div>
                </div>
            </div>
        </footer>
    </main>

    <!-- Core Local Scripts -->
    <script src="lenis.min.js"></script>
    <script src="gsap.min.js"></script>
    <script src="ScrollTrigger.min.js"></script>

    <!-- Three.js Scene Engine & Interactive Motion Masterpiece -->
    <script>
        const THREE = window.THREE;
        const GLTFLoader = window.GLTFLoader;
        const RoomEnvironment = window.RoomEnvironment;

        gsap.registerPlugin(ScrollTrigger);

        // Deterministic testing / debug parameter hook (?debug=1)
        const urlParams = new URLSearchParams(window.location.search);
        // Eliminate frame-skip jitter when syncing Lenis smooth scroll with GSAP ScrollTrigger
        gsap.ticker.lagSmoothing(0);

        // Initialize Lenis Smooth Scroll
        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            direction: 'vertical',
            gestureDirection: 'vertical',
            smooth: true,
            mouseMultiplier: 1.0,
            smoothTouch: false,
            touchMultiplier: 2,
            infinite: false,
        });

        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => {
            lenis.raf(time * 1000);
        });

        // Kinetic text roll generator
        function initKineticButtons() {
            const targets = document.querySelectorAll('.kinetic-text');
            targets.forEach(el => {
                const text = el.getAttribute('data-text') || el.textContent.trim();
                el.innerHTML = '';
                const chars = text.split('');
                chars.forEach((c, idx) => {
                    const charWrap = document.createElement('span');
                    charWrap.className = 'kinetic-char';
                    charWrap.style.transitionDelay = `${idx * 0.014}s`;
                    const primary = document.createElement('span');
                    primary.className = 'char-primary';
                    primary.textContent = c === ' ' ? '\u00A0' : c;
                    const secondary = document.createElement('span');
                    secondary.className = 'char-secondary';
                    secondary.textContent = c === ' ' ? '\u00A0' : c;
                    charWrap.appendChild(primary);
                    charWrap.appendChild(secondary);
                    el.appendChild(charWrap);
                });
            });
        }

        // Overlay menu controls
        function setupOverlay() {
            const toggle = document.getElementById('menu-toggle');
            const close = document.getElementById('menu-close');
            const overlay = document.getElementById('menu-overlay');
            const backdrop = document.getElementById('overlay-backdrop');
            const panel = document.getElementById('overlay-panel');

            if (!toggle || !overlay || !panel) return;

            let isOpen = false;

            function openMenu() {
                isOpen = true;
                overlay.classList.add('is-active');
                overlay.setAttribute('aria-hidden', 'false');
                toggle.setAttribute('aria-expanded', 'true');
                lenis.stop();
                gsap.to(backdrop, { opacity: 1, duration: 0.45, ease: 'power2.out' });
                gsap.to(panel, { x: '0%', duration: 0.65, ease: 'power4.out' });
            }

            function closeMenu() {
                isOpen = false;
                overlay.setAttribute('aria-hidden', 'true');
                toggle.setAttribute('aria-expanded', 'false');
                gsap.to(backdrop, {
                    opacity: 0,
                    duration: 0.35,
                    ease: 'power2.in',
                    onComplete: () => {
                        overlay.classList.remove('is-active');
                        lenis.start();
                    }
                });
                gsap.to(panel, { x: '100%', duration: 0.45, ease: 'power3.in' });
            }

            toggle.addEventListener('click', openMenu);
            if (close) close.addEventListener('click', closeMenu);
            if (backdrop) backdrop.addEventListener('click', closeMenu);

            document.querySelectorAll('.menu-link').forEach(link => {
                link.addEventListener('click', closeMenu);
            });
        }

        // Hero Entrance (Navbar elements enter cleanly; logo sits statically in middle of header)
        function setupHeroEntrance() {
            gsap.set('#main-brand-logo', {
                y: 0,
                scale: 1,
                opacity: 1,
                clearProps: 'transform'
            });

            const tl = gsap.timeline({ delay: 0.1 });

            tl.from(['.nav-left', '#main-brand-logo', '.nav-right'], {
                y: -20,
                opacity: 0,
                duration: 0.75,
                stagger: 0.08,
                ease: 'power3.out'
            })
                .from('.headline-word', {
                    yPercent: 110,
                    stagger: 0.08,
                    duration: 0.75,
                    ease: 'power4.out'
                }, '-=0.4')
                .from('.headline-tag, .hero-desc, .cta-group', {
                    y: 15,
                    opacity: 0,
                    stagger: 0.08,
                    duration: 0.65,
                    ease: 'power3.out'
                }, '-=0.5')
                .from('.cursive-annotation', {
                    opacity: 0,
                    y: 12,
                    stagger: 0.1,
                    duration: 0.6,
                    ease: 'power3.out'
                }, '-=0.5');
        }

        initKineticButtons();
        setupOverlay();
        setupHeroEntrance();

        // --- 1. THREE.JS SCENE SETUP ---
        const container = document.getElementById('webgl-container');
        const scene = new THREE.Scene();

        // Responsive Device Mode & Coordinate System
        function getDeviceMode() {
            const w = window.innerWidth;
            if (w < 768) return 'mobile';
            if (w <= 1024) return 'tablet';
            return 'desktop';
        }

        function getResponsiveCameraZ() {
            const w = window.innerWidth;
            const h = window.innerHeight;
            const aspect = w / h;
            if (w < 768) {
                if (aspect < 0.65) return 9.8;
                if (aspect < 1.0) return 8.8;
                return 7.6;
            } else if (w <= 1024) {
                return aspect < 1.0 ? 8.5 : 7.8;
            } else {
                return (h <= 800) ? 7.6 : 7.4;
            }
        }

        function getResponsiveBottleScale() {
            const w = window.innerWidth;
            const h = window.innerHeight;
            const aspect = w / h;
            if (w < 480) return 0.027;
            if (w < 768) return 0.030;
            if (w <= 1024) return aspect < 1.0 ? 0.032 : 0.035;
            if (h <= 800) return 0.034;
            return 0.038;
        }

        function getResponsiveOrbitScale() {
            const w = window.innerWidth;
            const h = window.innerHeight;
            if (w < 768) return 0.45;
            if (w <= 1024) return 0.65;
            if (h <= 800) return 0.75;
            return 0.85;
        }

        function getStageCoordinates() {
            const w = window.innerWidth;
            const h = window.innerHeight;
            const aspect = w / h;
            const mode = getDeviceMode();
            const camZ = getResponsiveCameraZ();

            const fovRad = (30 * Math.PI) / 180;
            const halfHeight = Math.tan(fovRad / 2) * camZ;
            const halfWidth = halfHeight * aspect;

            let heroX = 0;
            let heroY = 0;

            const calloutsEl = document.querySelector('.product-callouts');
            if (calloutsEl && mode !== 'mobile' && !(mode === 'tablet' && aspect < 1.0)) {
                const rect = calloutsEl.getBoundingClientRect();
                const targetScreenX = rect.left + rect.width * 0.52;
                const targetScreenY = h * 0.50;

                const ndcX = (targetScreenX / w) * 2 - 1;
                const ndcY = -(targetScreenY / h) * 2 + 1;

                heroX = Number((ndcX * halfWidth).toFixed(3));
                heroY = Number((ndcY * halfHeight).toFixed(3));
            } else if (mode === 'mobile') {
                heroX = 0.0;
                heroY = 0.28;
            } else if (mode === 'tablet' && aspect < 1.0) {
                heroX = 0.0;
                heroY = 0.20;
            } else {
                const contentWidth = Math.min(w * 0.9, 1540);
                const leftMargin = (w - contentWidth) / 2;
                const col1Width = contentWidth * 0.55;
                const col1CenterX = leftMargin + (col1Width * 0.52);
                const col1CenterY = h * 0.50;

                const ndcX = (col1CenterX / w) * 2 - 1;
                const ndcY = -(col1CenterY / h) * 2 + 1;

                heroX = Number((ndcX * halfWidth).toFixed(3));
                heroY = Number((ndcY * halfHeight).toFixed(3));
            }

            let storyAX = (mode === 'mobile' || (mode === 'tablet' && aspect < 1.0)) ? 0.0 : 1.25;
            let storyAY = (mode === 'mobile') ? 0.28 : (mode === 'tablet' && aspect < 1.0 ? 0.20 : 0.0);

            let storyBX = 0.0;
            let storyBY = (mode === 'mobile') ? -0.10 : -0.22;

            return {
                hero: { x: heroX, y: heroY },
                storyATravel: { startX: heroX, endX: storyAX, startY: heroY, endY: storyAY },
                storyA: { x: storyAX, y: storyAY },
                storyB: { x: storyBX, y: storyBY },
                ritualsDrop: -5.5
            };
        }

        let cachedStageCoordinates = getStageCoordinates();
        function updateCachedCoordinates() {
            cachedStageCoordinates = getStageCoordinates();
            return cachedStageCoordinates;
        }
        const initialCoords = cachedStageCoordinates;
        const camera = new THREE.PerspectiveCamera(30, window.innerWidth / window.innerHeight, 0.1, 100);
        camera.position.set(0, 0, getResponsiveCameraZ());

        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.05;
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        container.appendChild(renderer.domElement);

        // Studio PMREM Reflections
        const pmrem = new THREE.PMREMGenerator(renderer);
        pmrem.compileEquirectangularShader();
        const room = new RoomEnvironment();
        scene.environment = pmrem.fromScene(room, 0.04).texture;

        // --- 2. STUDIO LIGHTING ---
        const ambLight = new THREE.AmbientLight(0xf4efe6, 0.5);
        scene.add(ambLight);

        const keyLight = new THREE.DirectionalLight(0xfffaee, 2.1);
        keyLight.position.set(3.5, 4.5, 3.5);
        keyLight.castShadow = true;
        keyLight.shadow.mapSize.width = 2048;
        keyLight.shadow.mapSize.height = 2048;
        keyLight.shadow.bias = -0.0001;
        scene.add(keyLight);

        const fillLight = new THREE.DirectionalLight(0xdfeadc, 0.9);
        fillLight.position.set(-4.5, 2.0, 2.5);
        scene.add(fillLight);

        const rimLight = new THREE.DirectionalLight(0x8C9A5B, 3.8);
        rimLight.position.set(-3.5, 3.5, -3.5);
        scene.add(rimLight);

        const backRim = new THREE.DirectionalLight(0xD9962F, 1.8);
        backRim.position.set(3.2, -1.5, -3.5);
        scene.add(backRim);

        // Soft ground contact shadow
        const shadowPlaneGeo = new THREE.PlaneGeometry(10, 10);
        const shadowPlaneMat = new THREE.ShadowMaterial({ opacity: 0.22 });
        const shadowPlane = new THREE.Mesh(shadowPlaneGeo, shadowPlaneMat);
        shadowPlane.rotation.x = -Math.PI / 2;
        shadowPlane.position.set(initialCoords.hero.x, initialCoords.hero.y - (34.8 * getResponsiveBottleScale()), 0);
        shadowPlane.receiveShadow = true;
        scene.add(shadowPlane);

        // --- 3. REFINED GRAPHIC ORBIT RINGS ---
        const ringGeo = new THREE.TorusGeometry(1.95, 0.0045, 16, 128);
        const ringMat = new THREE.MeshBasicMaterial({
            color: 0xF3EFE6,
            transparent: true,
            opacity: 0.45,
            side: THREE.DoubleSide
        });
        const orbitRing = new THREE.Mesh(ringGeo, ringMat);
        orbitRing.rotation.x = Math.PI / 3.8;
        orbitRing.rotation.y = -Math.PI / 7;
        orbitRing.position.set(initialCoords.hero.x, initialCoords.hero.y, -0.8);
        const initRingScale = getResponsiveOrbitScale();
        orbitRing.scale.set(initRingScale, initRingScale, initRingScale);
        scene.add(orbitRing);

        const ringGeo2 = new THREE.TorusGeometry(2.15, 0.002, 16, 128);
        const ringMat2 = new THREE.MeshBasicMaterial({
            color: 0x8C9A5B,
            transparent: true,
            opacity: 0.25,
            side: THREE.DoubleSide
        });
        const orbitRing2 = new THREE.Mesh(ringGeo2, ringMat2);
        orbitRing2.rotation.x = Math.PI / 3.2;
        orbitRing2.rotation.y = -Math.PI / 5;
        orbitRing2.position.set(initialCoords.hero.x, initialCoords.hero.y, -0.9);
        orbitRing2.scale.set(initRingScale, initRingScale, initRingScale);
        scene.add(orbitRing2);

        // --- 4. PRODUCT GROUP ---
        // productGroup: master world transform (controlled EXCLUSIVELY by ScrollTrigger)
        const productGroup = new THREE.Group();
        productGroup.position.set(initialCoords.hero.x, initialCoords.hero.y, 0);
        productGroup.rotation.set(0.06, 0.12, -0.05);
        scene.add(productGroup);

        // bottleFloatGroup: child group dedicated to local ambient breathing & hovering
        // (Local coordinate space: zero conflict with world scroll transforms)
        const bottleFloatGroup = new THREE.Group();
        productGroup.add(bottleFloatGroup);

        window.productGroup = productGroup;
        window.bottleFloatGroup = bottleFloatGroup;
        window.orbitRing = orbitRing;
        window.orbitRing2 = orbitRing2;



        function base64ToArrayBuffer(base64) {
            const binaryString = window.atob(base64);
            const len = binaryString.length;
            const bytes = new Uint8Array(len);
            for (let i = 0; i < len; i++) {
                bytes[i] = binaryString.charCodeAt(i);
            }
            return bytes.buffer;
        }

        // --- 5. TEXTURE & MATERIAL PIPELINE ---
        const textureLoader = new THREE.TextureLoader();

        const labelSrc = (typeof window !== 'undefined' && window.REWAVE_LABEL_BASE64) ? window.REWAVE_LABEL_BASE64 : 'rewave_label_ultra_4k.png';
        const labelTex = textureLoader.load(labelSrc);
        labelTex.colorSpace = THREE.SRGBColorSpace;
        labelTex.flipY = true;
        labelTex.generateMipmaps = true;
        labelTex.minFilter = THREE.LinearMipmapLinearFilter;
        labelTex.magFilter = THREE.LinearFilter;
        try {
            labelTex.anisotropy = renderer.capabilities.getMaxAnisotropy();
        } catch (e) { }

        const condSrc = (typeof window !== 'undefined' && window.REWAVE_CONDENSATION_BASE64) ? window.REWAVE_CONDENSATION_BASE64 : 'condensation_normal.png';
        const condNormal = textureLoader.load(condSrc);
        condNormal.wrapS = THREE.RepeatWrapping;
        condNormal.wrapT = THREE.RepeatWrapping;
        condNormal.repeat.set(1.5, 3.0);

        // Crystal-clear PET plastic outer shell
        const matPlastic = new THREE.MeshPhysicalMaterial({
            color: 0xffffff,
            transmission: 0.98,
            opacity: 1,
            transparent: true,
            roughness: 0.03,
            metalness: 0.0,
            ior: 1.51,
            thickness: 0.35,
            specularIntensity: 1.3,
            clearcoat: 1.0,
            clearcoatRoughness: 0.02,
            normalMap: condNormal,
            normalScale: new THREE.Vector2(0.03, 0.03),
            envMapIntensity: 1.4,
            depthWrite: false
        });

        // Cold-Pressed Kiwi-Cucumber functional wellness juice with physical depth
        const matLiquid = new THREE.MeshPhysicalMaterial({
            color: 0x7EAA45,
            transmission: 0.86,
            opacity: 1,
            transparent: true,
            roughness: 0.10,
            metalness: 0.0,
            ior: 1.345,
            thickness: 2.8,
            attenuationColor: new THREE.Color(0x2E4D1A),
            attenuationDistance: 0.65,
            envMapIntensity: 1.2
        });

        const matCap = new THREE.MeshStandardMaterial({
            color: 0x12261C,
            roughness: 0.42,
            metalness: 0.08,
            envMapIntensity: 0.6
        });

        const matLabel = new THREE.MeshStandardMaterial({
            map: labelTex,
            roughness: 0.42,
            metalness: 0.0,
            transparent: true,
            depthWrite: true,
            alphaTest: 0.05,
            polygonOffset: true,
            polygonOffsetFactor: -1.0,
            polygonOffsetUnits: -1.0
        });

        // --- 6. MODEL LOADER ---
        let bottleMeshRoot = null;
        let capMeshRoot = null;
        let juiceMeshRoot = null;
        let capRestY = 31.56947;
        const gltfLoader = new GLTFLoader();

        function applyModelMaterials(gltf) {
            const root = gltf.scene;
            bottleMeshRoot = root;

            root.traverse((child) => {
                if (child.isMesh) {
                    child.castShadow = true;
                    child.receiveShadow = true;
                    if (child.name.includes('Cap')) {
                        capMeshRoot = child;
                        capRestY = child.position.y || 31.56947;
                        child.material = matCap;
                        child.renderOrder = 4;
                    } else if (child.name.includes('BottlePlastic')) {
                        child.material = matPlastic;
                        child.renderOrder = 3;
                        matPlastic.depthWrite = false;
                        matPlastic.transparent = true;
                    } else if (child.name.includes('Juice')) {
                        juiceMeshRoot = child;
                        child.material = matLiquid;
                        child.renderOrder = 1;
                        matLiquid.depthWrite = true;
                        matLiquid.transparent = true;
                        // Mathematical inset: depth 11.91 * 0.935 = 11.136 < label depth 11.25
                        child.scale.set(0.935, 0.985, 0.935);
                    } else if (child.name.includes('Label')) {
                        child.material = matLabel;
                        child.renderOrder = 2;
                    } else {
                        child.material = matCap;
                    }
                }
            });

            const bScale = getResponsiveBottleScale();
            root.scale.set(bScale, bScale, bScale);
            root.position.set(0, 0, 0);
            bottleFloatGroup.add(root);

            setupInteractiveMotion();
        }

        // Try direct memory parse first (zero-CORS offline & file:/// execution)
        if (typeof window !== 'undefined' && window.REWAVE_GLB_BASE64) {
            try {
                const buffer = base64ToArrayBuffer(window.REWAVE_GLB_BASE64);
                gltfLoader.parse(buffer, '', (gltf) => {
                    applyModelMaterials(gltf);
                }, (err) => {
                    console.warn('Memory parse fallback to URL load:', err);
                    loadFromUrl();
                });
            } catch (e) {
                console.warn('Buffer decode error, fallback to URL load:', e);
                loadFromUrl();
            }
        } else {
            loadFromUrl();
        }

        function loadFromUrl() {
            gltfLoader.load('assets/rewave_bottle.opt.glb', (gltf) => {
                applyModelMaterials(gltf);
            }, undefined, (error) => {
                console.error('GLB Load error:', error);
                setupInteractiveMotion();
            });
        }

        // --- 7. MASTER SCROLL CHOREOGRAPHY ---
        function setupInteractiveMotion() {
            const coords = getStageCoordinates();

            // Ambient floating is decoupled to local bottleFloatGroup in the unified render loop,
            // preventing any property collision with ScrollTrigger world positioning!

            // Orbit rings slow rotation
            gsap.to(orbitRing.rotation, {
                z: Math.PI * 2,
                duration: 32,
                repeat: -1,
                ease: 'none'
            });
            gsap.to(orbitRing2.rotation, {
                z: -Math.PI * 2,
                duration: 45,
                repeat: -1,
                ease: 'none'
            });

            // Stage Background Reference
            const stageBg = document.getElementById('stage-bg');

            // --- 1. IN-BETWEEN SCROLLTRIGGER: HERO -> STORY A (TRAVEL ZONE) ---
            ScrollTrigger.create({
                trigger: '#matrix',
                start: 'top bottom',
                end: 'top top',
                scrub: true,
                invalidateOnRefresh: true,
                onUpdate: (self) => {
                    const currentCoords = cachedStageCoordinates;
                    const p = self.progress;

                    const curX = currentCoords.storyATravel.startX + p * (currentCoords.storyATravel.endX - currentCoords.storyATravel.startX);
                    const curY = currentCoords.storyATravel.startY + p * (currentCoords.storyATravel.endY - currentCoords.storyATravel.startY);
                    productGroup.position.x = curX;
                    productGroup.position.y = curY;
                    productGroup.rotation.z = (1 - p) * (-0.05);
                    productGroup.rotation.x = (1 - p) * (0.06);
                    productGroup.scale.set(1, 1, 1);
                    productGroup.visible = true;
                    if (bottleMeshRoot) {
                        const bScale = getResponsiveBottleScale();
                        bottleMeshRoot.scale.set(bScale, bScale, bScale);
                    }
                    if (capMeshRoot) {
                        capMeshRoot.position.y = capRestY;
                        capMeshRoot.rotation.y = 0;
                    }
                    shadowPlane.position.x = curX;
                    shadowPlane.position.y = curY - (34.8 * getResponsiveBottleScale());

                    // Orbit rings fade out gently during transit
                    gsap.set(orbitRing.material, { opacity: Math.max(0, 0.45 * (1 - p)) });
                    gsap.set(orbitRing2.material, { opacity: Math.max(0, 0.25 * (1 - p)) });

                    // Stage background shifts seamlessly from Sage to Warm Bone
                    if (stageBg) {
                        stageBg.style.backgroundColor = p >= 0.5 ? 'var(--warm-bone)' : 'var(--sage-bg)';
                    }
                }
            });

            // --- 2. PINNED SCROLLTRIGGER: STORY A ("FUNCTIONAL BY DESIGN") ---
            ScrollTrigger.create({
                trigger: '#matrix',
                start: 'top top',
                end: () => (window.innerWidth < 768 ? '+=1800' : '+=2400'),
                pin: true,
                scrub: true,
                invalidateOnRefresh: true,
                onUpdate: (self) => {
                    const currentCoords = cachedStageCoordinates;
                    const p = self.progress;

                    productGroup.position.x = currentCoords.storyA.x;
                    productGroup.position.y = currentCoords.storyA.y;
                    productGroup.rotation.z = 0;
                    productGroup.rotation.x = 0;
                    productGroup.scale.set(1, 1, 1);
                    productGroup.visible = true;
                    if (bottleMeshRoot) {
                        const bScale = getResponsiveBottleScale();
                        bottleMeshRoot.scale.set(bScale, bScale, bScale);
                    }
                    if (capMeshRoot) {
                        capMeshRoot.position.y = capRestY;
                        capMeshRoot.rotation.y = 0;
                    }
                    shadowPlane.position.x = currentCoords.storyA.x;
                    shadowPlane.position.y = currentCoords.storyA.y - (34.8 * getResponsiveBottleScale());

                    if (stageBg) {
                        stageBg.style.backgroundColor = 'var(--warm-bone)';
                    }
                    gsap.set(orbitRing.material, { opacity: 0 });
                    gsap.set(orbitRing2.material, { opacity: 0 });

                    // Four quarter-turns across the pinned timeline (360 degrees rotation)
                    const rotY = 0.12 + (p * Math.PI * 2);
                    productGroup.rotation.y = rotY;

                    // Sequential Highlight for the 4 Benefit Statements
                    const statements = [
                        document.getElementById('stmt-1'),
                        document.getElementById('stmt-2'),
                        document.getElementById('stmt-3'),
                        document.getElementById('stmt-4')
                    ];

                    const activeIdx = Math.min(3, Math.floor(p * 4));

                    statements.forEach((stmt, idx) => {
                        if (!stmt) return;
                        if (idx === activeIdx) {
                            stmt.classList.add('active');
                            stmt.classList.remove('dimmed');
                        } else {
                            stmt.classList.remove('active');
                            stmt.classList.add('dimmed');
                        }
                    });
                }
            });

            // --- MASTER SCROLLTRIGGER: STORY B ("THE DECONSTRUCTED MATRIX") ---
            const storyBAccent = document.getElementById('story-b-accent');
            const storyBSpecs = document.getElementById('story-b-specs');
            const deconstructNodes = [
                document.getElementById('node-cap'),
                document.getElementById('node-kiwi'),
                document.getElementById('node-prebiotic'),
                document.getElementById('node-hydro')
            ];
            const isReducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

            ScrollTrigger.create({
                trigger: '#release',
                start: 'top top',
                end: () => (window.innerWidth < 768 ? '+=1800' : '+=2200'),
                pin: true,
                scrub: true,
                invalidateOnRefresh: true,
                onUpdate: (self) => {
                    const currentCoords = cachedStageCoordinates;
                    const p = self.progress;

                    // Dynamic rich dark theme flood
                    if (p >= 0.15) {
                        if (stageBg) stageBg.style.backgroundColor = 'var(--forest-green)';
                        document.documentElement.style.setProperty('--stage-fg', 'var(--warm-bone)');
                        document.documentElement.style.setProperty('--stage-fg-muted', 'rgba(243, 239, 230, 0.82)');
                        document.documentElement.style.setProperty('--stage-border', 'rgba(243, 239, 230, 0.16)');
                    } else {
                        if (stageBg) stageBg.style.backgroundColor = 'var(--warm-bone)';
                        document.documentElement.style.setProperty('--stage-fg', 'var(--forest-green)');
                        document.documentElement.style.setProperty('--stage-fg-muted', 'rgba(18, 38, 28, 0.78)');
                        document.documentElement.style.setProperty('--stage-border', 'rgba(18, 38, 28, 0.14)');
                    }

                    // Headline Accent: "THE RAW MATRIX." appears smoothly
                    if (storyBAccent) {
                        if (p >= 0.18) {
                            const accentProgress = Math.min(1, (p - 0.18) / 0.15);
                            if (isReducedMotion()) {
                                storyBAccent.style.opacity = '1';
                                storyBAccent.style.transform = 'none';
                            } else {
                                storyBAccent.style.opacity = accentProgress.toString();
                                storyBAccent.style.transform = `translateY(${(1 - accentProgress) * 8}px)`;
                            }
                        } else {
                            storyBAccent.style.opacity = '0';
                            if (!isReducedMotion()) {
                                storyBAccent.style.transform = 'translateY(8px)';
                            }
                        }
                    }

                    // Bottle moves seamlessly to center stage
                    const centerProgress = Math.min(1, p * 3.5);
                    const startX = currentCoords.storyA.x;
                    const targetX = currentCoords.storyB.x;
                    const startY = currentCoords.storyA.y;
                    const targetY = currentCoords.storyB.y;

                    productGroup.position.x = startX + centerProgress * (targetX - startX);
                    productGroup.position.y = startY + centerProgress * (targetY - startY);
                    productGroup.scale.set(1, 1, 1);
                    productGroup.visible = true;
                    if (bottleMeshRoot) {
                        const bScale = getResponsiveBottleScale();
                        bottleMeshRoot.scale.set(bScale, bScale, bScale);
                    }
                    shadowPlane.position.x = productGroup.position.x;
                    shadowPlane.position.y = productGroup.position.y - (34.8 * getResponsiveBottleScale());

                    // Precision Cap Lift: Cap unscrews and hovers weightlessly above bottle lip
                    if (capMeshRoot) {
                        if (p > 0.18 && p < 0.92) {
                            const capP = Math.min(1, Math.max(0, (p - 0.18) / 0.32));
                            capMeshRoot.position.y = capRestY + (capP * 13.5);
                            capMeshRoot.rotation.y = capP * Math.PI * 3;
                        } else if (p <= 0.18) {
                            capMeshRoot.position.y = capRestY;
                            capMeshRoot.rotation.y = 0;
                        } else if (p >= 0.92) {
                            // Settle cap back down before Rituals descent
                            const settleP = Math.min(1, (p - 0.92) / 0.08);
                            capMeshRoot.position.y = capRestY + ((1 - settleP) * 13.5);
                        }
                    }

                    // Subtle panoramic bottle micro-rotation: stays upright, elegant studio display
                    if (p > 0.20 && p < 0.90) {
                        const rotProgress = (p - 0.20) / 0.70;
                        productGroup.rotation.y = 0.12 + (rotProgress * 0.65);
                        productGroup.rotation.z = 0;
                        productGroup.rotation.x = 0.04;
                    } else if (p <= 0.20) {
                        productGroup.rotation.z = 0;
                        productGroup.rotation.x = 0;
                    }

                    // Staggered sequential illumination of the 4 Deconstruction Hotspots
                    const nodeThresholds = [0.20, 0.36, 0.54, 0.72];
                    deconstructNodes.forEach((node, idx) => {
                        if (!node) return;
                        const thresh = nodeThresholds[idx];
                        if (p >= thresh) {
                            const nodeP = Math.min(1, (p - thresh) / 0.12);
                            node.style.opacity = nodeP.toString();
                            node.style.transform = isReducedMotion() ? 'none' : `translateY(${(1 - nodeP) * 14}px)`;
                            if (idx === 3 || p < nodeThresholds[idx + 1]) {
                                node.classList.add('active');
                            } else {
                                node.classList.remove('active');
                            }
                        } else {
                            node.style.opacity = '0';
                            node.style.transform = isReducedMotion() ? 'none' : 'translateY(14px)';
                            node.classList.remove('active');
                        }
                    });

                    // Spec Strip reveals at bottom of section
                    if (storyBSpecs) {
                        if (p >= 0.78) {
                            const specProgress = Math.min(1, (p - 0.78) / 0.18);
                            storyBSpecs.style.opacity = specProgress.toString();
                            storyBSpecs.style.transform = isReducedMotion() ? 'none' : `translateY(${(1 - specProgress) * 6}px)`;
                        } else {
                            storyBSpecs.style.opacity = '0';
                            if (!isReducedMotion()) {
                                storyBSpecs.style.transform = 'translateY(6px)';
                            }
                        }
                    }
                }
            });

            // Interactive micro-focus when hovering / clicking deconstruction nodes
            deconstructNodes.forEach((node) => {
                if (!node) return;
                const comp = node.getAttribute('data-component');
                node.addEventListener('mouseenter', () => {
                    if (comp === 'cap' && capMeshRoot) {
                        gsap.to(capMeshRoot.position, { y: capRestY + 16.0, duration: 0.35, ease: 'power2.out' });
                    } else if (comp === 'kiwi') {
                        gsap.to(productGroup.rotation, { y: 0.45, duration: 0.4, ease: 'power2.out' });
                    } else if (comp === 'prebiotic') {
                        gsap.to(productGroup.rotation, { y: -0.15, duration: 0.4, ease: 'power2.out' });
                    } else if (comp === 'hydro') {
                        gsap.to(productGroup.rotation, { y: -0.45, duration: 0.4, ease: 'power2.out' });
                    }
                });
                node.addEventListener('mouseleave', () => {
                    if (comp === 'cap' && capMeshRoot) {
                        gsap.to(capMeshRoot.position, { y: capRestY + 13.5, duration: 0.35, ease: 'power2.out' });
                    }
                });
            });

            // Rituals ScrollTrigger: bottle gracefully descends on ALL screens so Ritual columns take the spotlight
            ScrollTrigger.create({
                trigger: '#rituals',
                start: 'top 85%',
                end: 'top 15%',
                scrub: true,
                invalidateOnRefresh: true,
                onUpdate: (self) => {
                    const currentCoords = cachedStageCoordinates;
                    const p = self.progress;
                    const startY = currentCoords.storyB.y;

                    productGroup.position.y = startY - (p * 5.0);
                    productGroup.visible = (p < 0.85);

                    productGroup.scale.setScalar(1 - p * 0.45);

                    if (shadowPlane && shadowPlane.material) {
                        shadowPlane.material.opacity = Math.max(0, 0.22 * (1 - p));
                    }

                    if (capMeshRoot) {
                        capMeshRoot.position.y = capRestY;
                        capMeshRoot.rotation.y = 0;
                    }
                }
            });

            // Explicit gsap.fromTo for Ritual Items to prevent any stuck opacity
            gsap.fromTo('.ritual-item',
                {
                    opacity: 0,
                    y: 40
                },
                {
                    scrollTrigger: {
                        trigger: '.rituals-grid',
                        start: 'top 85%',
                        end: 'bottom 60%',
                        toggleActions: 'play none none reverse'
                    },
                    opacity: 1,
                    y: 0,
                    duration: 0.85,
                    stagger: 0.15,
                    ease: 'power3.out'
                }
            );

            // Subtle mouse parallax
            let targetMouseX = 0;
            let targetMouseY = 0;
            window.addEventListener('mousemove', (e) => {
                const nx = (e.clientX / window.innerWidth) * 2 - 1;
                const ny = -(e.clientY / window.innerHeight) * 2 + 1;
                targetMouseX = nx * 0.12;
                targetMouseY = ny * 0.1;
            });

            gsap.ticker.add(() => {
                keyLight.position.x += (3.5 + targetMouseX * 3 - keyLight.position.x) * 0.05;
                keyLight.position.y += (4.5 + targetMouseY * 3 - keyLight.position.y) * 0.05;
            });

            // Master timeline scrub hook for deterministic testing
            window.__rewave = {
                setProgress(progress) {
                    const totalScroll = document.documentElement.scrollHeight - window.innerHeight;
                    window.scrollTo(0, progress * totalScroll);
                    ScrollTrigger.update();
                }
            };
        }

        // --- 8. RESIZE & FLUID DYNAMICS TICKER ---
        function handleResize() {
            const w = window.innerWidth;
            const h = window.innerHeight;
            const currentCoords = updateCachedCoordinates();
            const camZ = getResponsiveCameraZ();
            const bScale = getResponsiveBottleScale();
            const rScale = getResponsiveOrbitScale();

            camera.aspect = w / h;
            camera.position.z = camZ;
            camera.updateProjectionMatrix();
            renderer.setSize(w, h);

            if (bottleMeshRoot) {
                bottleMeshRoot.scale.set(bScale, bScale, bScale);
            }

            if (orbitRing && orbitRing2) {
                orbitRing.scale.set(rScale, rScale, rScale);
                orbitRing2.scale.set(rScale, rScale, rScale);
            }

            // Only reposition to hero defaults if user is near top of page
            if (window.scrollY < 80) {
                productGroup.scale.set(1, 1, 1);
                productGroup.visible = true;
                productGroup.position.x = currentCoords.hero.x;
                productGroup.position.y = currentCoords.hero.y;
                orbitRing.position.x = currentCoords.hero.x;
                orbitRing.position.y = currentCoords.hero.y;
                orbitRing2.position.x = currentCoords.hero.x;
                orbitRing2.position.y = currentCoords.hero.y;
                shadowPlane.position.x = currentCoords.hero.x;
                shadowPlane.position.y = currentCoords.hero.y - (34.8 * bScale);
            }

            ScrollTrigger.refresh();
        }

        window.addEventListener('resize', handleResize);
        window.addEventListener('orientationchange', () => {
            setTimeout(handleResize, 120);
        });

        // Fluid Physics & Kinetic Liquid Sloshing
        let lastScrollY = window.scrollY;
        let scrollVel = 0;
        let sloshRotZ = 0;
        let sloshRotX = 0;
        let sloshVelZ = 0;
        let sloshVelX = 0;

        function animate() {
            requestAnimationFrame(animate);
            const time = performance.now() * 0.001;

            // 1. Decoupled local ambient floating: active only in Hero, smoothly fades out on scroll
            const scrollY = window.scrollY || window.pageYOffset || 0;
            const heroFade = Math.max(0, 1 - scrollY / (window.innerHeight * 0.8));
            if (bottleFloatGroup) {
                if (heroFade > 0.001) {
                    bottleFloatGroup.position.y = Math.sin(time * 1.8) * 0.045 * heroFade;
                    bottleFloatGroup.rotation.z = Math.sin(time * 1.2) * 0.018 * heroFade;
                    bottleFloatGroup.rotation.x = Math.cos(time * 1.4) * 0.015 * heroFade;
                } else {
                    bottleFloatGroup.position.y = 0;
                    bottleFloatGroup.rotation.z = 0;
                    bottleFloatGroup.rotation.x = 0;
                }
            }

            // 2. Liquid meniscus physics - smoothly lerped
            const curY = window.scrollY;
            const sDelta = curY - lastScrollY;
            lastScrollY = curY;
            scrollVel += (sDelta * 0.002 - scrollVel) * 0.1;

            if (juiceMeshRoot && productGroup) {
                juiceMeshRoot.rotation.set(0, 0, 0);
                const clampedVel = Math.max(-0.015, Math.min(0.015, scrollVel * 0.01));
                const verticalBob = Math.sin(time * 2.2) * 0.005 - Math.abs(clampedVel);
                juiceMeshRoot.position.y = Math.max(-0.02, Math.min(0.02, verticalBob));
            }

            renderer.render(scene, camera);
        }

        // --- 9. REBUILT FOOTER MOTION & FORM VALIDATION ---
        function initFooterFeatures() {
            // Form validation
            const form = document.getElementById('footer-newsletter-form');
            const input = document.getElementById('footer-email-input');
            const feedback = document.getElementById('footer-form-feedback');
            const successBox = document.getElementById('footer-form-success');

            if (form && input && feedback && successBox) {
                form.addEventListener('submit', (e) => {
                    e.preventDefault();
                    const email = input.value.trim();
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!email || !emailRegex.test(email)) {
                        feedback.textContent = 'Please enter a valid email address.';
                        feedback.style.display = 'block';
                        input.setAttribute('aria-invalid', 'true');
                        input.focus();
                    } else {
                        feedback.textContent = '';
                        feedback.style.display = 'none';
                        input.removeAttribute('aria-invalid');
                        form.style.display = 'none';
                        successBox.style.display = 'block';
                    }
                });

                input.addEventListener('input', () => {
                    if (feedback.style.display === 'block') {
                        feedback.textContent = '';
                        feedback.style.display = 'none';
                        input.removeAttribute('aria-invalid');
                    }
                });
            }

            // Motion with GSAP
            const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            if (isReduced) return;

            if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
                // Image parallax: yPercent -4 -> 0, scale 1.06 -> 1, scrub
                gsap.fromTo('.footer-landscape-img',
                    {
                        yPercent: -4,
                        scale: 1.06,
                        transformOrigin: 'center bottom'
                    },
                    {
                        scrollTrigger: {
                            trigger: '#footer',
                            start: 'top bottom',
                            end: 'bottom bottom',
                            scrub: true
                        },
                        yPercent: 0,
                        scale: 1,
                        ease: 'power2.out'
                    }
                );

                // Headline lines slide up from a mask
                gsap.fromTo('.footer-headline-line',
                    {
                        yPercent: 100
                    },
                    {
                        scrollTrigger: {
                            trigger: '.footer-headline-wrap',
                            start: 'top 85%',
                            toggleActions: 'play none none reverse'
                        },
                        yPercent: 0,
                        duration: 0.9,
                        stagger: 0.12,
                        ease: 'power3.out'
                    }
                );

                // Columns fade up 16px with a small stagger
                gsap.fromTo('.footer-col',
                    {
                        opacity: 0,
                        y: 16
                    },
                    {
                        scrollTrigger: {
                            trigger: '.footer-main-row',
                            start: 'top 85%',
                            toggleActions: 'play none none reverse'
                        },
                        opacity: 1,
                        y: 0,
                        duration: 0.75,
                        stagger: 0.1,
                        ease: 'power2.out'
                    }
                );
            }
        }
        initFooterFeatures();

        animate();
    </script>
</body>

</html>'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"index.html successfully updated! Length: {len(HTML_CONTENT)} characters")
