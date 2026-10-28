def calculate_system_metrics(total_orders, defective_orders, processing_days):
    defect_rate = (float(defective_orders) / float(total_orders)) * 100.0 if float(total_orders) > 0 else 0.0
    average_lead_time = float(processing_days) / float(total_orders) if float(total_orders) > 0 else 0.0
    return defect_rate, average_lead_time
