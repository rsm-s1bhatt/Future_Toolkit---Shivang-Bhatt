import streamlit as st
from datetime import datetime, date, timedelta

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Before the Moment",
    page_icon="🕒",
    layout="wide",
)

# -------------------------------------------------
# SIDEBAR + GLOBAL STYLE (MATCHES HOME, NO SUBTITLE)
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

        /* -------- PAGE STYLE -------- */
        .section-title {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            margin-top: 0.6rem;
            margin-bottom: 0.3rem;
        }

        .section-title-text {
            font-size: 1.4rem;
            font-weight: 700;
            color: #e5e7eb;
        }

        .section-sub {
            font-size: 0.98rem;
            color: #9ca3af;
            margin-bottom: 0.9rem;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            padding: 0.18rem 0.55rem;
            border-radius: 999px;
            font-size: 0.72rem;
            letter-spacing: 0.03em;
            text-transform: uppercase;
            font-weight: 600;
            color: #e5e7eb;
        }

        .pill-small {
            background: rgba(56,189,248,0.15);
            border: 1px solid rgba(56,189,248,0.5);
        }

        .prepcard {
            border-radius: 0.9rem;
            padding: 1.0rem 1.1rem;
            background: linear-gradient(135deg, rgba(15,23,42,0.95), rgba(15,23,42,0.9));
            border: 1px solid rgba(148,163,184,0.4);
        }

        .prepcard-title {
            font-size: 1.05rem;
            font-weight: 600;
            color: #e5e7eb;
            margin-bottom: 0.3rem;
        }

        .prepcard-sub {
            font-size: 0.86rem;
            color: #9ca3af;
            margin-bottom: 0.6rem;
        }

        .prepcard-label {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: #9ca3af;
            margin-top: 0.6rem;
            margin-bottom: 0.1rem;
        }

        .prepcard-text {
            font-size: 0.95rem;
            color: #e5e7eb;
        }
    </style>

    <!-- Sidebar Header -->
    <div class="sidebar-header-wrap">
        <div class="sidebar-title">
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
# PAGE HEADER
# -------------------------------------------------
st.markdown(
    """
    <div class="section-title">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="9" stroke="#38bdf8" stroke-width="1.8"/>
            <path d="M12 7 v5 l3 2" stroke="#22c55e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="12" cy="12" r="2.2" fill="#0f172a" stroke="#f97373" stroke-width="1.4"/>
        </svg>
        <div class="section-title-text">Before the Moment</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="section-sub">
A page for preparing before something actually happens – so Future You has a fair shot at showing up.
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------
# INPUTS
# -------------------------------------------------
left, right = st.columns([1.1, 0.9])

with left:
    st.markdown(
        '<span class="pill pill-small">Step 1 · Describe the moment</span>',
        unsafe_allow_html=True,
    )
    st.markdown("### What’s coming up?")

    title = st.text_input(
        "Short name for this moment",
        placeholder="e.g., Check-in with manager, Project pitch, Difficult conversation",
    )

    default_date = date.today() + timedelta(days=1)
    when = st.date_input("When is it?", value=default_date)

    stakes = st.select_slider(
        "How important does this feel right now?",
        options=["Low", "Medium", "High", "Very high"],
        value="Medium",
    )

    people = st.text_input(
        "Who else is involved?",
        placeholder="Names / roles, e.g. manager, teammate, recruiter",
    )

    context = st.text_area(
        "What’s the basic situation?",
        placeholder="One or two sentences about what’s going on.",
        height=90,
    )

    st.markdown("---")
    st.markdown(
        '<span class="pill pill-small">Step 2 · Past pattern</span>',
        unsafe_allow_html=True,
    )
    st.markdown("### What usually happens?")

    pattern = st.text_area(
        "When you’ve been in similar situations before, what did Past You tend to do?",
        placeholder="e.g., avoid raising concerns, talk too fast, downplay my own ideas...",
        height=80,
    )

    worst_fear = st.text_input(
        "If this goes badly, what are you worried might happen?",
        placeholder="Say the part you’d usually keep in your head.",
    )

with right:
    st.markdown(
        '<span class="pill pill-small">Step 3 · Future You’s plan</span>',
        unsafe_allow_html=True,
    )
    st.markdown("### How do you want to show up this time?")

    intent = st.text_area(
        "If this went surprisingly well, what would Future You be proud of?",
        placeholder="e.g., I was direct but respectful; I asked for what I actually wanted...",
        height=90,
    )

    focus = st.multiselect(
        "What do you want to lean into?",
        options=[
            "Listening first",
            "Being clear about what I want",
            "Stating my point of view calmly",
            "Asking good questions",
            "Backing my ideas with examples",
            "Making the other person feel seen",
        ],
        default=["Listening first"],
    )

    small_move = st.text_area(
        "One small, concrete move you can make in the moment:",
        placeholder="e.g., Open with a question instead of a pitch; write down 3 bullet points beforehand...",
        height=80,
    )

    give_first = st.text_area(
        "If you wanted to 'give first' in this moment, what could that look like?",
        placeholder="A small way to make their life easier before you ask for anything.",
        height=80,
    )

# -------------------------------------------------
# PREP CARD
# -------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div class="section-title">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
            <rect x="3" y="4" width="18" height="16" rx="3" fill="#0f172a" stroke="#22c55e" stroke-width="1.6"/>
            <path d="M7 10 H17" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round"/>
            <path d="M7 14 H13" stroke="#f97373" stroke-width="1.4" stroke-linecap="round"/>
        </svg>
        <div class="section-title-text">Prep Card for Future You</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if title or context or intent:
    with st.container():
        st.markdown('<div class="prepcard">', unsafe_allow_html=True)

        heading = title if title else "This moment"
        when_str = when.strftime("%b %d, %Y") if isinstance(when, date) else str(when)

        st.markdown(
            f"""
            <div class="prepcard-title">{heading}</div>
            <div class="prepcard-sub">Date: {when_str} · Stakes: {stakes}</div>
            """,
            unsafe_allow_html=True,
        )

        if context:
            st.markdown(
                '<div class="prepcard-label">Context</div>', unsafe_allow_html=True
            )
            st.markdown(
                f'<div class="prepcard-text">{context}</div>', unsafe_allow_html=True
            )

        if people:
            st.markdown(
                '<div class="prepcard-label">Who matters here</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="prepcard-text">{people}</div>', unsafe_allow_html=True
            )

        if pattern:
            st.markdown(
                '<div class="prepcard-label">Past pattern</div>', unsafe_allow_html=True
            )
            st.markdown(
                f'<div class="prepcard-text">{pattern}</div>', unsafe_allow_html=True
            )

        if worst_fear:
            st.markdown(
                '<div class="prepcard-label">What you’re worried about</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="prepcard-text">{worst_fear}</div>', unsafe_allow_html=True
            )

        if intent:
            st.markdown(
                '<div class="prepcard-label">Future You’s intention</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="prepcard-text">{intent}</div>', unsafe_allow_html=True
            )

        if focus:
            st.markdown(
                '<div class="prepcard-label">Things to lean into</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="prepcard-text">' + ", ".join(focus) + "</div>",
                unsafe_allow_html=True,
            )

        if small_move:
            st.markdown(
                '<div class="prepcard-label">First small move</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="prepcard-text">{small_move}</div>', unsafe_allow_html=True
            )

        if give_first:
            st.markdown(
                '<div class="prepcard-label">Give first</div>', unsafe_allow_html=True
            )
            st.markdown(
                f'<div class="prepcard-text">{give_first}</div>', unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info(
        "Fill in a few fields above and this section will turn into a one-page prep card for Future You."
    )
