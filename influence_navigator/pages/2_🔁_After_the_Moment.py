import streamlit as st
from datetime import date
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="After the Moment",
    page_icon="🔁",
    layout="wide",
)

# -------------------------------------------------
# SIDEBAR + GLOBAL STYLE (MATCHES HOME)
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

        .logcard {
            border-radius: 0.9rem;
            padding: 1.0rem 1.1rem;
            background: linear-gradient(135deg, rgba(15,23,42,0.95), rgba(15,23,42,0.9));
            border: 1px solid rgba(148,163,184,0.4);
            margin-bottom: 0.6rem;
        }

        .logcard-title {
            font-size: 1.0rem;
            font-weight: 600;
            color: #e5e7eb;
            margin-bottom: 0.15rem;
        }

        .logcard-sub {
            font-size: 0.8rem;
            color: #9ca3af;
            margin-bottom: 0.4rem;
        }

        .logcard-label {
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: #9ca3af;
            margin-top: 0.45rem;
            margin-bottom: 0.08rem;
        }

        .logcard-text {
            font-size: 0.9rem;
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
# SESSION STATE FOR LOGGING
# -------------------------------------------------
if "after_log" not in st.session_state:
    st.session_state.after_log = []

# -------------------------------------------------
# PAGE HEADER
# -------------------------------------------------
st.markdown(
    """
    <div class="section-title">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="9" stroke="#38bdf8" stroke-width="1.8"/>
            <path d="M8 10 L6 8 L8 6" stroke="#f97373" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M16 14 L18 16 L16 18" stroke="#22c55e" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M7 13 C7.8 15, 9.7 16.5, 12 16.5 C14.3 16.5, 16.2 15, 17 13" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round"/>
        </svg>
        <div class="section-title-text">After the Moment</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="section-sub">
A page for replaying what actually happened and spotting patterns in whether Past, Present, or Future You showed up.
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------
# INPUT FORM
# -------------------------------------------------
st.markdown(
    '<span class="pill pill-small">Step 1 · Capture what happened</span>',
    unsafe_allow_html=True,
)
st.markdown("### Quick reflection")

col1, col2 = st.columns([1.1, 0.9])

with col1:
    moment_title = st.text_input(
        "What moment are you reflecting on?",
        placeholder="e.g., 1:1 with manager, conversation with teammate, client call",
    )

    when = st.date_input("When did it happen?", value=date.today())

    went_scale = st.slider(
        "If 1 is 'I’m not proud of how I showed up' and 10 is 'This is exactly how I want Future Me to act', where was this?",
        min_value=1,
        max_value=10,
        value=6,
    )

    who_showed = st.radio(
        "Who showed up most in this moment?",
        options=["Past Me", "Present Me", "Future Me"],
        horizontal=True,
    )

    what_happened = st.text_area(
        "What actually happened?",
        placeholder="Just a few bullet points of what you did and how the other person responded.",
        height=110,
    )

with col2:
    felt_like = st.text_area(
        "What did it feel like from the inside?",
        placeholder="Nerves, emotions, thoughts running through your head...",
        height=90,
    )

    good = st.text_area(
        "What went better than you expected?",
        placeholder="Moments you want to repeat next time.",
        height=80,
    )

    different = st.text_area(
        "If you could replay this with Future You in charge, what would be different?",
        placeholder="Specific sentences, questions, or moves you’d change.",
        height=80,
    )

    tiny_experiment = st.text_input(
        "One tiny experiment for next time:",
        placeholder="Something 1% different you can try in the next similar moment.",
    )

saved = False
if st.button("Save this reflection"):
    if moment_title or what_happened:
        st.session_state.after_log.insert(
            0,
            {
                "title": moment_title or "Unnamed moment",
                "when": when,
                "score": went_scale,
                "who": who_showed,
                "what": what_happened,
                "felt": felt_like,
                "good": good,
                "different": different,
                "experiment": tiny_experiment,
            },
        )
        saved = True
        st.success(
            "Saved. Future You can now scroll down and see this in the pattern log."
        )
    else:
        st.warning("Add at least a title or description before saving.")

st.markdown("---")

# -------------------------------------------------
# LOG + PATTERN VIEW
# -------------------------------------------------
st.markdown(
    """
    <div class="section-title">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
            <rect x="3" y="4" width="18" height="16" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="1.6"/>
            <path d="M7 15 C8 13, 9.5 12, 12 12 C14.5 12, 16 13, 17 15" stroke="#22c55e" stroke-width="1.4" stroke-linecap="round"/>
            <circle cx="9" cy="10" r="1.3" fill="#f97373"/>
            <circle cx="15" cy="10" r="1.3" fill="#f97373"/>
        </svg>
        <div class="section-title-text">Pattern log</div>
    </div>
    """,
    unsafe_allow_html=True,
)

log = st.session_state.after_log

if not log:
    st.info(
        "Once you save a reflection above, it will show up here so you can see patterns over time."
    )
else:
    # Simple stats row
    total = len(log)
    past_count = sum(1 for r in log if r["who"] == "Past Me")
    present_count = sum(1 for r in log if r["who"] == "Present Me")
    future_count = sum(1 for r in log if r["who"] == "Future Me")

    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        st.metric("Reflections saved", total)
    with col_b:
        st.metric("Past Me showed up", past_count)
    with col_c:
        st.metric("Present Me showed up", present_count)
    with col_d:
        st.metric("Future Me showed up", future_count)

    st.markdown("")

    # Display each log entry
    for idx, entry in enumerate(log):
        with st.container():
            st.markdown('<div class="logcard">', unsafe_allow_html=True)

            when_str = (
                entry["when"].strftime("%b %d, %Y")
                if isinstance(entry["when"], date)
                else str(entry["when"])
            )
            st.markdown(
                f"""
                <div class="logcard-title">{entry["title"]}</div>
                <div class="logcard-sub">
                    {when_str} · Rating: {entry["score"]}/10 · Most prominent: {entry["who"]}
                </div>
                """,
                unsafe_allow_html=True,
            )

            if entry["what"]:
                st.markdown(
                    '<div class="logcard-label">What happened</div>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<div class="logcard-text">{entry["what"]}</div>',
                    unsafe_allow_html=True,
                )

            if entry["felt"]:
                st.markdown(
                    '<div class="logcard-label">From the inside</div>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<div class="logcard-text">{entry["felt"]}</div>',
                    unsafe_allow_html=True,
                )

            if entry["good"]:
                st.markdown(
                    '<div class="logcard-label">Keep this</div>', unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="logcard-text">{entry["good"]}</div>',
                    unsafe_allow_html=True,
                )

            if entry["different"]:
                st.markdown(
                    '<div class="logcard-label">Next-time edit</div>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<div class="logcard-text">{entry["different"]}</div>',
                    unsafe_allow_html=True,
                )

            if entry["experiment"]:
                st.markdown(
                    '<div class="logcard-label">Tiny experiment</div>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<div class="logcard-text">{entry["experiment"]}</div>',
                    unsafe_allow_html=True,
                )

            st.markdown("</div>", unsafe_allow_html=True)

        # Bar chart
st.markdown("---")
st.markdown("### How often each version of me is showing up")

log = st.session_state.get("after_log", [])

if not log:
    st.info(
        "Once you’ve logged a few moments, this section will show you how often "
        "Past Me, Present Me, and Future Me have been running the show."
    )
else:
    # ---- Count how many times each version showed up ----
    who_list = []
    for entry in log:
        # Adjust this line if your key name is different
        who = entry.get("who_showed_up") or entry.get("who")
        if who:
            who_list.append(who)

    if not who_list:
        st.info("No 'who showed up' data yet — log a few more moments.")
    else:
        categories = ["Past Me", "Present Me", "Future Me"]
        counts = {c: 0 for c in categories}
        for w in who_list:
            if w in counts:
                counts[w] += 1

        df_counts = pd.DataFrame(
            {
                "Version": list(counts.keys()),
                "Times I Showed Up This Way": list(counts.values()),
            }
        ).set_index("Version")

        total = sum(counts.values())

        if total > 0:
            st.markdown(
                f"- **Past Me:** {counts['Past Me']} time(s)  \n"
                f"- **Present Me:** {counts['Present Me']} time(s)  \n"
                f"- **Future Me:** {counts['Future Me']} time(s)"
            )
            st.caption(
                "This isn’t about getting a perfect score — it’s just noticing the pattern "
                "so Future Me has an easier job next time."
            )

        # 🔹 Single bar chart – main visual
        st.bar_chart(df_counts, use_container_width=True)

        # 🔹 Optional: trend over time (if dates exist)
        dates = []
        version_for_trend = []

        for entry in log:
            raw_date = (
                entry.get("date")
                or entry.get("when")  # if you used 'when' as the field
                or entry.get("created_at")
                or entry.get("timestamp")
            )
            who = entry.get("who_showed_up") or entry.get("who")
            if raw_date and who in categories:
                dates.append(raw_date)
                version_for_trend.append(who)

        if dates:
            trend_df = pd.DataFrame({"date": dates, "who": version_for_trend})
            trend_df["date"] = pd.to_datetime(trend_df["date"], errors="coerce")
            trend_df = trend_df.dropna(subset=["date"])

            if not trend_df.empty:
                # Count per day per version
                daily_counts = (
                    trend_df.groupby(["date", "who"])
                    .size()
                    .unstack(fill_value=0)
                    .reindex(columns=categories, fill_value=0)
                )

                st.markdown("#### How the pattern is shifting over time")
                st.line_chart(daily_counts, use_container_width=True)
                st.caption(
                    "Each point is a day where you logged something. "
                    "The goal isn’t to make Past Me disappear overnight — "
                    "it’s just to see Future Me showing up a bit more often over time."
                )
