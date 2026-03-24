import streamlit as st
import json
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="GamingVault", page_icon="🎮", layout="wide")

# --- 2. PERSISTENCE FUNCTIONS ---
def load_library():
    if os.path.exists('game_library.json'):
        with open('game_library.json', 'r') as file:
            return json.load(file)
    return {}

def save_library(data):
    with open('game_library.json', 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

# Delete function
def delete_game(game_name):
    if game_name in st.session_state.library:
        del st.session_state.library[game_name]
        save_library(st.session_state.library)
        st.rerun()

# Load data at startup
if 'library' not in st.session_state:
    st.session_state.library = load_library()

# --- 3. INTERFACE: SIDEBAR ---
with st.sidebar:
    st.header("➕ Add New Game")
    with st.form("game_form", clear_on_submit=True):
        name = st.text_input("Game Name").strip().title()
        platform = st.selectbox("Platform", ["PC", "PS5", "XBOX", "SWITCH", "RETRO"])
        completed = st.checkbox("Completed? ✅")
        platinum = st.checkbox("Platinum? 🏆")
        
        btn_add = st.form_submit_button("Save to Vault")
        
        if btn_add and name:
            st.session_state.library[name] = {
                'platform': platform,
                'completed': completed,
                'platinum': platinum
            }
            save_library(st.session_state.library)
            st.success(f"¡{name} added!")
            st.rerun()

# --- 4. MAIN BODY ---
st.title("🎮 GamingVault: Your Game Collection")

# Statistics
total = len(st.session_state.library)
completed_count = sum(1 for j in st.session_state.library.values() if j['completed'])
platinum_count = sum(1 for j in st.session_state.library.values() if j['platinum'])

col_a, col_b, col_c = st.columns(3)
col_a.metric("Total Games", total)
col_b.metric("Completed", completed_count)
col_c.metric("Platinums", platinum_count)

st.divider()

# Search Bar
search = st.text_input("🔍 Search for a game in your collection...", "").strip().title()

# Filter and Display
filtered_data = {k: v for k, v in st.session_state.library.items() if search in k}

if filtered_data:
    # Table Header
    c1, c2, c3, c4 = st.columns([3, 2, 2, 2])
    c1.write("**Name**")
    c2.write("**Platform**")
    c3.write("**Status**")
    c4.write("**Actions**")
    
    for game_name, info in filtered_data.items():
        col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
        
        with col1:
            st.write(game_name)
        with col2:
            st.write(info['platform'])
        with col3:
            # --- CUMULATIVE STATUS LOGIC ---
            status_icons = []
            if info['completed']:
                status_icons.append("✅ Completed")
            if info['platinum']:
                status_icons.append("🏆 Platinum")
            
            if not status_icons:
                st.write("⏳ Pending")
            else:
                st.write(" / ".join(status_icons))
                
        with col4:
            # --- ACTIONS COLUMN (EDIT & DELETE) ---
            col_edit, col_delete = st.columns(2)
            
            with col_delete:
                if st.button("🗑️", key=f"delete_{game_name}"):
                    delete_game(game_name)

            with col_edit:
                # --- EDIT POP-OVER ---
                with st.popover("📝", help=f"Edit {game_name}"):
                    st.subheader(f"Edit: {game_name}")
                    
                    with st.form(key=f"edit_form_{game_name}"):
                        new_name = st.text_input("Name", value=game_name).strip().title()
                        new_platform = st.selectbox(
                            "Platform", 
                            ["PC", "PS5", "XBOX", "SWITCH", "RETRO"],
                            index=["PC", "PS5", "XBOX", "SWITCH", "RETRO"].index(info['platform'])
                        )
                        new_completed = st.checkbox("Completed?", value=info['completed'])
                        new_platinum = st.checkbox("Platinum?", value=info['platinum'])
                        
                        btn_save_edit = st.form_submit_button("Save Changes")

                        if btn_save_edit:
                            # 1. Delete old entry
                            del st.session_state.library[game_name]
                            
                            # 2. Create new entry
                            st.session_state.library[new_name] = {
                                'platform': new_platform,
                                'completed': new_completed,
                                'platinum': new_platinum
                            }
                            
                            # 3. Save and rerun
                            save_library(st.session_state.library)
                            st.success(f"¡{new_name} updated!")
                            st.rerun()
else:
    st.info("No games found matching your search.")
