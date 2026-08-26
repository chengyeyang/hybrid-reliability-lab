def filter_records(records, selected_outcome):
    if selected_outcome == "All":
        return records
    else:
        return [
            record
            for record in records
            if record.outcome == selected_outcome
        ]


def format_pass_rate(pass_rate):
    if pass_rate is None:
        return "N/A"
    else:
        return f"{(pass_rate * 100):.1f}%"
