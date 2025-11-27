import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Future Shivang’s Toolkit",
    page_icon="🧭",
    layout="wide",
)

# -------------------------------------------------
# UNIFIED SIDEBAR + GLOBAL STYLE (NO SUBTITLE)
# -------------------------------------------------
st.markdown(
    """
    <style>
        /* -------- SIDEBAR -------- */
        [data-testid="stSidebar"] {
            background: radial-gradient(circle at top left, #0f172a 0, #020617 60%) !important;
            border-right: 1px solid #1f2937 !important;
        }

        [data-testid="stSidebarNav"] > ul {
            margin-top: 0.7rem;
        }

        .sidebar-header-wrap {
            padding: 1.0rem 0.75rem 0.5rem 0.75rem;
        }

        .sidebar-title {
            font-size: 1.28rem;
            font-weight: 700;
            color: #e5e7eb;
            display: flex;
            align-items: center;
            gap: 0.55rem;
            margin-bottom: 0.2rem;
        }

        .sidebar-divider {
            height: 1px;
            background: linear-gradient(to right, transparent, #1f2937, transparent);
            margin: 0.55rem 0.6rem 0.2rem 0.6rem;
        }

        [data-testid="stSidebarNav"] ul li a {
            border-radius: 0.55rem;
            padding: 0.38rem 0.75rem !important;
            margin: 0.12rem 0.45rem !important;
            font-size: 0.93rem;
            font-weight: 500 !important;
            color: #e5e7eb !important;
            display: flex;
            align-items: center;
            gap: 0.45rem;
        }

        [data-testid="stSidebarNav"] ul li a:hover {
            background-color: rgba(56, 189, 248, 0.12) !important;
            color: #38bdf8 !important;
        }

        [data-testid="stSidebarNav"] ul li a[aria-current="page"] {
            background: linear-gradient(90deg, rgba(56,189,248,0.16), rgba(34,197,94,0.16));
            border: 1px solid rgba(148,163,184,0.5);
        }

        /* -------- MAIN PAGE GLOBAL STYLE -------- */
        .section-title {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            margin-top: 1.8rem;
            margin-bottom: 0.3rem;
        }

        .section-title:first-of-type {
            margin-top: 0.8rem;
        }

        .section-title-text {
            font-size: 1.4rem;
            font-weight: 700;
            color: #e5e7eb;
        }

        .section-title-sub {
            font-size: 1.0rem;
            color: #9ca3af;
            margin-bottom: 0.8rem;
        }

        .page-subtle-quote {
            font-size: 0.9rem;
            color: #9ca3af;
            font-style: italic;
            margin-top: 0.4rem;
        }
    </style>

    <!-- Sidebar Header WITHOUT subtitle -->
    <div class="sidebar-header-wrap">
        <div class="sidebar-title">
            <!-- Multi-colour SVG logo -->
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <circle cx="12" cy="12" r="10" stroke="#38bdf8" stroke-width="2"/>
              <path d="M12 6 L16 12 L12 18 L8 12 Z" fill="#22c55e"/>
              <circle cx="12" cy="12" r="3" fill="#f97373"/>
            </svg>
            <span>Future Shivang’s Toolkit</span>
        </div>
    </div>

    <div class="sidebar-divider"></div>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# MAIN PAGE CONTENT
# -------------------------------------------------

# ---------- SECTION 1: Welcome ----------
st.markdown(
    """
    <div class="section-title">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
            <rect x="3" y="4" width="18" height="16" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="1.6"/>
            <path d="M6 9 H18" stroke="#22c55e" stroke-width="1.4" stroke-linecap="round"/>
            <circle cx="8" cy="7" r="1" fill="#38bdf8"/>
            <circle cx="12" cy="7" r="1" fill="#f97373"/>
            <circle cx="16" cy="7" r="1" fill="#22c55e"/>
        </svg>
        <div class="section-title-text">Welcome to the Toolkit</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
This is a small two–page space for practicing how **Future You** wants to show up.

Use the sidebar to jump into:
- **Before the Moment** – prepare before something important
- **After the Moment** – reflect on how you handled it afterward
"""
)

st.markdown("---")

# ---------- SECTION 2: Three Versions of Me ----------
st.markdown(
    """
    <div class="section-title">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
            <circle cx="6" cy="12" r="3" fill="#64748b"/>
            <circle cx="12" cy="12" r="3" fill="#38bdf8"/>
            <circle cx="18" cy="12" r="3" fill="#22c55e"/>
        </svg>
        <div class="section-title-text">The Three Versions of Me</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
In almost every important moment, one of three versions of you tends to show up:
"""
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Past Me")
    st.caption("Autopilot mode")
    st.markdown(
        """
- Reacts without much preparation
- Avoids discomfort or tough conversations
- Often thinks later: *“Why did I say/do that?”*
"""
    )

with col2:
    st.markdown("#### Present Me")
    st.caption("Reflective mode")
    st.markdown(
        """
- Notices what felt off after the moment
- Replays conversations in my head
- Starts to see patterns in how I show up
"""
    )

with col3:
    st.markdown("#### Future Me")
    st.caption("Intentional mode")
    st.markdown(
        """
- Prepares before moments that matter
- Makes small, deliberate moves
- Tries to shift the pattern 1% at a time
"""
    )

st.markdown(
    """
<div class="page-subtle-quote">
“​The biggest predictor of influence is not personality, but whether you act with intention.” – course idea, rewritten for myself
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("---")

# ---------- SECTION 3: Two Tools ----------
st.markdown(
    """
    <div class="section-title">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
            <rect x="3" y="5" width="18" height="14" rx="3" fill="#0f172a" stroke="#22c55e" stroke-width="1.6"/>
            <path d="M7 9 H17" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round"/>
            <path d="M7 13 H13" stroke="#f97373" stroke-width="1.4" stroke-linecap="round"/>
        </svg>
        <div class="section-title-text">The Two Tools in This Toolkit</div>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2)

with left:
    st.markdown("#### Before the Moment")
    st.caption("A page for preparing before something actually happens.")
    st.markdown(
        """
Use this when you have something on the calendar that matters:

- A conversation you're nervous about
- A team or project meeting
- An interview or networking chat
- A conflict you've been avoiding

**What it helps you do:**
- Turn a vague situation into a clear description
- Guess what the other person might actually want
- Write a simple rehearsal of how Future You wants to show up

Open it from the left sidebar: **Before the Moment**.
"""
    )

with right:
    st.markdown("#### After the Moment")
    st.caption("A page for replaying realistic scenarios and spotting patterns.")
    st.markdown(
        """
Use this when you want to practice your instincts without real-world pressure:

- Answer short, realistic scenarios
- See whether Past, Present, or Future Me showed up
- Notice which tactics you naturally use (or avoid)

**What it helps you do:**
- Build language for what actually happened
- See tiny shifts in your choices over time
- Make it easier for Future Me to choose differently next time

Open it from the left sidebar: **After the Moment**.
"""
    )

st.markdown("---")

# ---------- SECTION 4: Why This Exists ----------
st.markdown(
    """
    <div class="section-title">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
            <path d="M4 19 C5 15, 7 7, 12 5 C16 7, 19 11, 20 19" stroke="#38bdf8" stroke-width="1.6" fill="none"/>
            <circle cx="12" cy="9" r="2" fill="#f97373"/>
            <path d="M10.5 14 H13.5 V18 H10.5 Z" fill="#22c55e"/>
        </svg>
        <div class="section-title-text">Why This Exists for Future Shivang</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
I’ve noticed that the biggest gap in my life isn’t knowing concepts —
it’s applying them **in the moment** when it matters.

This toolkit is my attempt to close that gap by giving myself two tiny spaces:

1. One to prepare **before** important moments
2. One to reflect **after** them

If Future Me uses these even a few times a year, it will already have been worth building.
"""
)
