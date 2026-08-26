import streamlit as st
from src.visualization.report_visualization import plot_outcome, plot_measurements
from src.dashboard.sample_data import report, records
from src.dashboard.dashboard_helpers import filter_records, format_pass_rate


st.title("Hardware Test Dashboard")
st.subheader("Overall Test Summary")

summary_columns = st.columns(2)

with summary_columns[0]:
    st.metric("Total Tests", report.total_tests)

with summary_columns[1]:
    pass_rate_display = format_pass_rate(report.pass_rate)

    st.metric("Pass Rate", pass_rate_display)

outcome_columns = st.columns(3)

with outcome_columns[0]:
    st.metric("PASS", report.pass_count)

with outcome_columns[1]:
    st.metric("FAIL", report.fail_count)

with outcome_columns[2]:
    st.metric("ERROR", report.error_count)

st.subheader("Outcome Distribution")
fig, _ = plot_outcome(report)
st.pyplot(fig)

st.subheader("Measurement Summary")
fig, _ = plot_measurements(report)
st.pyplot(fig)

st.subheader("Failure Information")
if not report.failure_details:
    st.success("No failures")
else:
    st.dataframe(report.failure_details)

st.subheader("Test History")
selected_outcome = st.selectbox(
    "Outcome",
    ["All", "PASS", "FAIL", "ERROR"],
)

filtered_records = filter_records(records, selected_outcome)

history_data = [
    {
        "Test Name": filtered_record.test_name,
        "Outcome": filtered_record.outcome,
        "Measurement": filtered_record.measurement,
        "Duration": filtered_record.duration,
        "Error": filtered_record.error,
    }
    for filtered_record in filtered_records
]

if not records:
    st.write("No test history available.")
elif not history_data:
    st.write("No records match the selected filter.")
else:
    st.dataframe(history_data)

