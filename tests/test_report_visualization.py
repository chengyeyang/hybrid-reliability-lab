from src.visualization.report_visualization import plot_outcome, plot_measurements
from src.report.test_report import OneTestReport
import matplotlib.pyplot as plt


def make_test_report(
    total_tests=10,
    pass_count=6,
    fail_count=3,
    error_count=1,
    pass_rate=0.6,
    measurement_count=3,
    minimum_measurement=2,
    maximum_measurement=8,
    average_measurement=5,
    failure_details=None,
):
    return OneTestReport(
        total_tests=total_tests,
        pass_count=pass_count,
        fail_count=fail_count,
        error_count=error_count,
        pass_rate=pass_rate,
        measurement_count=measurement_count,
        minimum_measurement=minimum_measurement,
        maximum_measurement=maximum_measurement,
        average_measurement=average_measurement,
        failure_details=[] if failure_details is None else failure_details,
    )


def test_plot_outcome_maps_values_to_correct_labels():
    report = make_test_report()

    fig, ax = plot_outcome(report)

    texts = [text.get_text() for text in ax.texts]

    assert texts[0] == "PASS"
    assert texts[1] == "FAIL"
    assert texts[2] == "ERROR"
    assert texts[3] == "60.0%"
    assert texts[4] == "30.0%"
    assert texts[5] == "10.0%"

    plt.close(fig)


def test_plot_outcome_handles_zero_count_category():
    report = make_test_report(
        pass_count=6,
        fail_count=4,
        error_count=0
)

    fig, ax = plot_outcome(report)

    texts = [text.get_text() for text in ax.texts]

    assert texts[0] == "PASS"
    assert texts[1] == "FAIL"
    assert texts[2] == "ERROR"
    assert texts[3] == "60.0%"
    assert texts[4] == "40.0%"
    assert texts[5] == "0.0%"

    plt.close(fig)


def test_plot_outcome_shows_no_test_data_for_empty_report():
    report = make_test_report(
        total_tests=0,
)

    fig, ax = plot_outcome(report)

    texts = [text.get_text() for text in ax.texts]

    assert len(texts) == 1
    assert texts[0] == "No test data"

    plt.close(fig)


def test_plot_measurements_maps_values_to_correct_labels():
    report = make_test_report(
        minimum_measurement=1,
        maximum_measurement=8,
        average_measurement=2,
)

    fig, ax = plot_measurements(report)
    bars = ax.patches
    heights = [bar.get_height() for bar in bars]
    labels = [label.get_text() for label in ax.get_xticklabels()]

    assert labels[0] == "Minimum"
    assert labels[1] == "Average"
    assert labels[2] == "Maximum"

    assert heights[0] == 1
    assert heights[1] == 2
    assert heights[2] == 8

    plt.close(fig)


def test_plot_measurements_handles_zero_measurement_value():
    report = make_test_report(
        minimum_measurement=0,
        maximum_measurement=8,
        average_measurement=2,
)

    fig, ax = plot_measurements(report)
    bars = ax.patches
    heights = [bar.get_height() for bar in bars]
    labels = [label.get_text() for label in ax.get_xticklabels()]

    assert labels[0] == "Minimum"
    assert labels[1] == "Average"
    assert labels[2] == "Maximum"

    assert heights[0] == 0
    assert heights[1] == 2
    assert heights[2] == 8

    plt.close(fig)


def test_plot_measurements_shows_no_measurement_data_when_empty():
    report = make_test_report(
        measurement_count=0,
)

    fig, ax = plot_measurements(report)

    assert len(ax.texts) == 1
    assert ax.texts[0].get_text() == "No measurement data"
    assert len(ax.patches) == 0

    plt.close(fig)
