import pandas as pd
import time
import numpy as np
from tqdm import tqdm
import os

# Define file paths
base_path = r'c:\\Users\\14987\\Desktop\\JobMarketIreland_dataAnalystProject\\datasets'
raw_path = os.path.join(base_path, 'raw')
cleaned_path = os.path.join(base_path, 'cleanedData', 'overAll')

# Predefined coordinates for Irish cities and locations
IRELAND_COORDINATES = {
    'Dublin': (53.3498, -6.2603),
    'Cork': (51.8985, -8.4756),
    'Galway': (53.2707, -9.0568),
    'Limerick': (52.6638, -8.6267),
    'Waterford': (52.2593, -7.1101),
    'Kilkenny': (52.6541, -7.2448),
    'Wexford': (52.3369, -6.4633),
    'Sligo': (54.2766, -8.4761),
    'Drogheda': (53.7189, -6.3478),
    'Dundalk': (54.0043, -6.4058),
    'Bray': (53.2026, -6.0983),
    'Navan': (53.6527, -6.6802),
    'Ennis': (52.8438, -8.9864),
    'Tralee': (52.2713, -9.7016),
    'Carlow': (52.8407, -6.9269),
    'Naas': (53.2157, -6.6669),
    'Athlone': (53.4239, -7.9407),
    'Letterkenny': (54.9503, -7.7342),
    'Tullamore': (53.2740, -7.4896),
    'Killarney': (52.0599, -9.5044),
    'Arklow': (52.7918, -6.1536),
    'Cobh': (51.8503, -8.2959),
    'Castlebar': (53.8567, -9.2985),
    'Midleton': (51.9156, -8.1794),
    'Mallow': (52.1326, -8.6419),
    'Ballina': (54.1167, -9.1500),
    'Enniscorthy': (52.5020, -6.5581),
    'Wicklow': (52.9808, -6.0331),
    'Cavan': (53.9909, -7.3601),
    'Monaghan': (54.2492, -6.9683),
    'Carrick-on-Shannon': (53.9472, -8.0928),
    'Birr': (53.0955, -7.9123),
    'Kinsale': (51.7058, -8.5311),
    'Youghal': (51.9506, -7.8506),
    'Bantry': (51.6781, -9.4561),
    'Skibbereen': (51.5500, -9.2667),
    'Clonakilty': (51.6231, -8.8706),
    'Dungarvan': (52.0881, -7.6256),
    'Lismore': (52.1394, -7.9347),
    'Cashel': (52.5158, -7.8856),
    'Clonmel': (52.3558, -7.7036),
    'Thurles': (52.6811, -7.8122),
    'Nenagh': (52.8619, -8.1975),
    'Roscrea': (52.9519, -7.8019),
    'Portlaoise': (53.0344, -7.2994),
    'Mountmellick': (53.1131, -7.3244),
    'Mullingar': (53.5264, -7.3386),
    'Longford': (53.7289, -7.7956),
    'Roscommon': (53.6331, -8.1869),
    'Boyle': (53.9719, -8.2969),
    'Strokestown': (53.7831, -8.0956),
    'Ballymote': (54.0833, -8.5167),
    'Tuam': (53.5167, -8.8500),
    'Ballinasloe': (53.3281, -8.2181),
    'Loughrea': (53.1969, -8.5681),
    'Gort': (53.0667, -8.8167),
    'Clifden': (53.4889, -10.0203),
    'Westport': (53.8000, -9.5167),
    'Belmullet': (54.2167, -9.9833),
    'Ballyhaunis': (53.7667, -8.7667),
    'Claremorris': (53.7167, -9.0000),
    'Swinford': (53.9333, -8.9500),
    'Knock': (53.7833, -8.9167),
    'Charleville': (52.3500, -8.6833),
    'Fermoy': (52.1369, -8.2756),
    'Mitchelstown': (52.2667, -8.2667),
    'Macroom': (51.9000, -8.9500),
    'Bandon': (51.7472, -8.7394),
    'Clonakilty': (51.6231, -8.8706),
    'Dunmanway': (51.7167, -9.1167),
    'Schull': (51.5333, -9.5333),
    'Castletownbere': (51.6500, -9.9000),
    'Kenmare': (51.8833, -9.5833),
    'Cahersiveen': (51.9500, -10.2167),
    'Dingle': (52.1406, -10.2681),
    'Listowel': (52.4500, -9.4833),
    'Castleisland': (52.2333, -9.4667),
    'Kilorglin': (52.1000, -9.7833),
    'Milltown': (52.0833, -9.8000),
    'Sneem': (51.8333, -9.9000),
    'Waterville': (51.8333, -10.1667),
    'Ballyshannon': (54.5000, -8.1833),
    'Bundoran': (54.4833, -8.2833),
    'Donegal': (54.6500, -8.1167),
    'Glenties': (54.7833, -8.2833),
    'Dungloe': (55.0500, -8.3500),
    'Gweedore': (55.0500, -8.2167),
    'Milford': (55.1167, -7.6833),
    'Ramelton': (55.0333, -7.6500),
    'Buncrana': (55.1333, -7.4500),
    'Carndonagh': (55.2500, -7.2667),
    'Moville': (55.1833, -7.0333),
    'Malin': (55.3667, -7.3667),
    'Ballybofey': (54.8000, -7.7833),
    'Stranorlar': (54.8000, -7.7667),
    'Lifford': (54.8333, -7.4833),
    'Castlefin': (54.8667, -7.6000),
    'Convoy': (54.8667, -7.6333),
    'Raphoe': (54.8833, -7.5833),
    'Ballindrait': (54.8833, -7.4833),
    'St Johnston': (54.9000, -7.4500),
    'Newtowncunningham': (54.9833, -7.4167),
    'Muff': (55.0667, -7.2500),
    'Quigley\'s Point': (55.1000, -7.1833),
    'Greencastle': (55.2000, -7.0333),
    'Culdaff': (55.2833, -7.2167),
    'Clonmany': (55.2833, -7.3000),
    'Ballyliffin': (55.3167, -7.3667),
    'Malin Head': (55.3833, -7.3667),
    # Remote work locations
    'Remote': (53.3498, -6.2603),  # Default to Dublin coordinates
    'Work from Home': (53.3498, -6.2603),
    'Hybrid': (53.3498, -6.2603),
    'Ireland': (53.1424, -7.6921),  # Center of Ireland
    'Nationwide': (53.1424, -7.6921),
    'Multiple Locations': (53.1424, -7.6921)
}

# Read the three CSV files
print("Reading CSV files...")
da_df = pd.read_csv(os.path.join(raw_path, 'DA_job_data.csv'))
de_df = pd.read_csv(os.path.join(raw_path, 'DE_job_data.csv'))
ds_df = pd.read_csv(os.path.join(raw_path, 'DS_job_data.csv'))

# Add job type column to distinguish the data sources
da_df['job_type'] = 'DA'
de_df['job_type'] = 'DE'
ds_df['job_type'] = 'DS'

# Combine all dataframes
print("Combining dataframes...")
all_jobs_df = pd.concat([da_df, de_df, ds_df], ignore_index=True)
print(f"Total combined records: {len(all_jobs_df)}")
print(f"Column names: {list(all_jobs_df.columns)}")

# Check if job_location column exists
if 'job_location' not in all_jobs_df.columns:
    print("Error: 'job_location' column not found")
    print(f"Available columns: {list(all_jobs_df.columns)}")
    exit()

# Display sample locations
print("\nLocation samples:")
print(all_jobs_df['job_location'].head(10).tolist())

def get_coordinates_from_dict(location):
    """Get latitude and longitude from predefined dictionary"""
    if pd.isna(location) or location == '':
        return pd.Series([None, None])
    
    location_str = str(location).strip()
    
    # Direct match
    if location_str in IRELAND_COORDINATES:
        coords = IRELAND_COORDINATES[location_str]
        return pd.Series([coords[0], coords[1]])
    
    # Try partial matching (case insensitive)
    location_lower = location_str.lower()
    for city, coords in IRELAND_COORDINATES.items():
        if city.lower() in location_lower or location_lower in city.lower():
            return pd.Series([coords[0], coords[1]])
    
    # If no match found, try to extract city name from common patterns
    # Remove common suffixes like ", Ireland", ", Co. Cork", etc.
    clean_location = location_str.replace(", Ireland", "").replace(", Co.", "").strip()
    
    # Try matching the cleaned location
    for city, coords in IRELAND_COORDINATES.items():
        if city.lower() == clean_location.lower():
            return pd.Series([coords[0], coords[1]])
    
    # If still no match, default to Dublin coordinates and log
    print(f"Location not found in dictionary: {location_str}, defaulting to Dublin")
    return pd.Series([53.3498, -6.2603])  # Dublin coordinates as default

# Get unique locations to show processing progress
unique_locations = all_jobs_df['job_location'].dropna().unique()
print(f"\nFound {len(unique_locations)} unique locations")

# Create location to coordinates mapping using dictionary
location_coords = {}
print("\nStarting coordinate mapping process...")

for i, location in enumerate(tqdm(unique_locations, desc="Mapping coordinates")):
    coords = get_coordinates_from_dict(location)
    location_coords[location] = coords
    
    # Show progress every 10 locations
    if (i + 1) % 10 == 0:
        successful = sum(1 for coords in location_coords.values() if not pd.isna(coords[0]))
        print(f"Processed {i + 1}/{len(unique_locations)} locations, successful: {successful}")

# Apply coordinates to original dataframe
print("\nApplying coordinates to dataframe...")
all_jobs_df['latitude'] = all_jobs_df['job_location'].map(lambda x: location_coords.get(x, pd.Series([None, None]))[0] if pd.notna(x) else None)
all_jobs_df['longitude'] = all_jobs_df['job_location'].map(lambda x: location_coords.get(x, pd.Series([None, None]))[1] if pd.notna(x) else None)

# Calculate statistics
successful_geocoding = all_jobs_df[['latitude', 'longitude']].dropna().shape[0]
print(f"\nCoordinate mapping completed:")
print(f"Total records: {len(all_jobs_df)}")
print(f"Successfully mapped: {successful_geocoding}")
print(f"Success rate: {successful_geocoding/len(all_jobs_df)*100:.1f}%")

# Show successful examples
print("\nSuccessful examples:")
success_examples = all_jobs_df[all_jobs_df['latitude'].notna()][['job_location', 'latitude', 'longitude', 'job_type']].head()
print(success_examples)

# Show unmapped locations for reference
unmapped_locations = all_jobs_df[all_jobs_df['latitude'].isna()]['job_location'].unique()
if len(unmapped_locations) > 0:
    print(f"\nUnmapped locations ({len(unmapped_locations)}):")
    for loc in unmapped_locations[:10]:  # Show first 10
        print(f"  - {loc}")
    if len(unmapped_locations) > 10:
        print(f"  ... and {len(unmapped_locations) - 10} more")

# Create output directory if it doesn't exist
os.makedirs(cleaned_path, exist_ok=True)

# Save to CSV file
output_csv_path = os.path.join(cleaned_path, 'All_job_data_with_coordinates.csv')
print(f"\nSaving to CSV: {output_csv_path}")
all_jobs_df.to_csv(output_csv_path, index=False)
print("CSV file saved successfully!")

# Also save a summary of unique locations with coordinates
location_summary = pd.DataFrame([
    {'location': loc, 'latitude': coords[0], 'longitude': coords[1]} 
    for loc, coords in location_coords.items()
])
location_summary_path = os.path.join(cleaned_path, 'Location_coordinates_summary.csv')
location_summary.to_csv(location_summary_path, index=False)
print(f"Location summary saved to: {location_summary_path}")

print("\nLocation transformation completed!")
print(f"Final dataset contains {len(all_jobs_df)} job records with coordinates")
print(f"Job type distribution:")
print(all_jobs_df['job_type'].value_counts())