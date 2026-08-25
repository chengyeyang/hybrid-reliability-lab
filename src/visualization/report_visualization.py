import matplotlib.pyplot as plt


def plot_outcome(report):
    fig, ax = plt.subplots()

    if report.total_tests == 0:
        ax.text(
            0.5,
            0.5,
            "No test data",
            ha="center",
            va="center"
        )

    else:
        values = [
            report.pass_count,
            report.fail_count,
            report.error_count
        ]

        labels = ["PASS", "FAIL", "ERROR"]

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

    ax.set_title("Test Result Distribution")

    return fig, ax


def plot_measurements(report):
    fig, ax = plt.subplots()

    if report.measurement_count == 0:
        ax.text(
            0.5,
            0.5,
            "No measurement data",
            ha="center",
            va="center"
        )
    else:
        values = [
            report.minimum_measurement,
            report.average_measurement,
            report.maximum_measurement
        ]

        labels = ["Minimum", "Average", "Maximum"]

        ax.bar(labels, values)

    ax.set_title(f"Test Measurement Summary\nMeasurement Count: {report.measurement_count}")

    return fig, ax
