def extrapolate_uptime_downtime(observations, business_hours):
    """
    :param observations: list of tuples containing observation time and status (up or down)
    :param business_hours: tuple containing start and end time of business hours
    :return: list of tuples containing time intervals and status (up or down)
    """
    start_time, end_time = business_hours
    extrapolated_data = []
    current_status = observations[0][1]
    current_start_time = start_time
    for observation in observations:
        observation_time, status = observation
        if status != current_status:
            extrapolated_data.append((current_start_time, observation_time, current_status))
            current_start_time = observation_time
            current_status = status
    extrapolated_data.append((current_start_time, end_time, current_status))
    return extrapolated_data
#
# Example usage:
observations = [('10:14', 'up'), ('11:15', 'down')]
business_hours = ('9:00', '12:00')
extrapolated_data = extrapolate_uptime_downtime(observations, business_hours)
print(extrapolated_data)
