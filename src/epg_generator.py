import json
from datetime import datetime, timedelta

# Function to generate EPG data

def generate_epg_data():
    current_time = datetime.utcnow()
    # Create a list to hold the programming data
    epg_data = []
    channels = [
        {'id': 1, 'name': 'Channel 1'},
        {'id': 2, 'name': 'Channel 2'},
        {'id': 3, 'name': 'Channel 3'},
    ]

    # Generate data for 7 days
    for day in range(7):
        date = current_time + timedelta(days=day)
        for channel in channels:
            # Sample programming data
            for program in range(3):  # 3 programs per day
                start_time = datetime.combine(date.date(), datetime.min.time()) + timedelta(hours=program * 2)
                end_time = start_time + timedelta(hours=2)
                epg_data.append({
                    'channel_id': channel['id'],
                    'channel_name': channel['name'],
                    'start': start_time.strftime('%Y%m%d%H%M%S +0000'),
                    'end': end_time.strftime('%Y%m%d%H%M%S +0000'),
                    'title': f'Program {program + 1} - {channel['name']}',
                    'description': f'Description for {channel['name']} - Program {program + 1}',
                })

    return epg_data

# Generate and print EPG JSON
if __name__ == '__main__':
    epg_json = generate_epg_data()
    print(json.dumps(epg_json, indent=4))