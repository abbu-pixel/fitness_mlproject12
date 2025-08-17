import streamlit as st
import joblib
import json
import numpy as np

# --- Load model + columns ---
@st.cache_data
def load_model():
    return joblib.load("model.pkl")

@st.cache_data
def load_model_columns():
    with open("model_columns.json", "r") as f:
        return json.load(f)

model = load_model()
model_columns = load_model_columns()

# --- Page Config ---
st.set_page_config(page_title="Fitbit Calories App", page_icon="🔥", layout="centered")
st.title("🔥 Fitbit Calories Prediction & Advice")
st.markdown("Predict calories burned, get exercise & diet advice, and track your steps!")

# --- Fitness Goal ---
goal = st.selectbox(
    "🎯 Select Your Fitness Goal",
    ["Maintain Weight", "Lose Weight", "Gain Muscle"]
)

# --- Input Dictionary ---
inputs = {}

# 🚶 Steps & Distance
with st.expander("🚶 Steps & Distance"):
    col1, col2 = st.columns(2)
    with col1:
        inputs["TotalSteps"] = st.slider("Total Steps", 0, 50000, 5000, step=100)
        inputs["TotalDistance"] = st.number_input("Total Distance (km)", value=3.0, step=0.1)
    with col2:
        inputs["TrackerDistance"] = st.number_input("Tracker Distance (km)", value=3.0, step=0.1)
        inputs["LoggedActivitiesDistance"] = st.number_input("Logged Activities Distance (km)", value=0.0, step=0.1)

# ⏱️ Activity Minutes
with st.expander("⏱️ Activity Minutes"):
    col1, col2 = st.columns(2)
    with col1:
        inputs["VeryActiveMinutes"] = st.slider("Very Active Minutes", 0, 300, 30, step=5)
        inputs["FairlyActiveMinutes"] = st.slider("Fairly Active Minutes", 0, 300, 20, step=5)
    with col2:
        inputs["LightlyActiveMinutes"] = st.slider("Lightly Active Minutes", 0, 600, 120, step=10)
        inputs["SedentaryMinutes"] = st.slider("Sedentary Minutes", 0, 1440, 600, step=10)

# 🏃 Active Distances
with st.expander("🏃 Active Distances (km)"):
    col1, col2 = st.columns(2)
    with col1:
        inputs["VeryActiveDistance"] = st.number_input("Very Active Distance", value=1.0, step=0.1)
        inputs["ModeratelyActiveDistance"] = st.number_input("Moderately Active Distance", value=1.0, step=0.1)
    with col2:
        inputs["LightActiveDistance"] = st.number_input("Light Active Distance", value=2.0, step=0.1)
        inputs["SedentaryActiveDistance"] = st.number_input("Sedentary Active Distance", value=0.0, step=0.1)

# --- Advice Logic ---
def get_advice(goal, calories):
    if goal == "Maintain Weight":
        return "✅ Maintain current activity and balanced diet."
    elif goal == "Lose Weight":
        return f"⚡ Burn more calories than consumed. You burned ~{calories:.0f} kcal today."
    elif goal == "Gain Muscle":
        return f"💪 Eat more calories than burned. You burned ~{calories:.0f} kcal today."

# --- Macronutrient Breakdown ---
def macronutrients(calories, goal):
    if goal == "Lose Weight":
        protein = 0.3 * calories
        carbs = 0.4 * calories
        fat = 0.3 * calories
    elif goal == "Gain Muscle":
        protein = 0.3 * calories
        carbs = 0.5 * calories
        fat = 0.2 * calories
    else:  # Maintain
        protein = 0.25 * calories
        carbs = 0.5 * calories
        fat = 0.25 * calories
    return protein, carbs, fat

# --- Workout Suggestions ---
def workout_suggestions(goal):
    if goal == "Lose Weight":
        return "🏃 Cardio: running, cycling, HIIT 3-5x/week\n🏋️ Strength: light resistance training 2-3x/week"
    elif goal == "Gain Muscle":
        return "🏋️ Strength training 3-5x/week\n🏃 Light cardio 1-2x/week"
    else:  # Maintain
        return "🏃 Mix of moderate cardio and light strength training 3x/week"

# --- Step / Distance Goals ---
def step_goals(total_steps, total_distance):
    recommended_steps = 7000
    recommended_distance = 5.0  # km
    step_msg = f"You walked {total_steps} steps. Aim for {recommended_steps} steps tomorrow."
    distance_msg = f"You covered {total_distance:.2f} km. Aim for {recommended_distance} km tomorrow."
    return step_msg, distance_msg

# --- Prediction ---
if st.button("🔮 Predict Calories & Get Advice"):
    try:
        # Validation
        total_active_distance = (
            inputs["VeryActiveDistance"] +
            inputs["ModeratelyActiveDistance"] +
            inputs["LightActiveDistance"] +
            inputs["SedentaryActiveDistance"]
        )
        if not np.isclose(total_active_distance, inputs["TotalDistance"], atol=0.5):
            st.warning(
                f"⚠️ Sum of active distances ({total_active_distance:.2f} km) "
                f"does not match Total Distance ({inputs['TotalDistance']} km)."
            )

        # Predict calories
        input_data = np.array([[inputs.get(col, 0) for col in model_columns]])
        prediction = model.predict(input_data)[0]
        st.success(f"🔥 Estimated Calories Burned: **{prediction:.2f} kcal**")
        st.balloons()

        # Show advice
        st.markdown("### 📝 Exercise & Diet Advice")
        st.info(get_advice(goal, prediction))

        # Macronutrients
        protein, carbs, fat = macronutrients(prediction, goal)
        st.markdown("### 🍽️ Suggested Macronutrients")
        st.write(f"Protein: {protein:.0f} kcal | Carbs: {carbs:.0f} kcal | Fat: {fat:.0f} kcal")

        # Workout suggestions
        st.markdown("### 🏋️ Personalized Workout Suggestions")
        st.info(workout_suggestions(goal))

        # Step / Distance goals
        st.markdown("### 👣 Step & Distance Goals")
        step_msg, distance_msg = step_goals(inputs["TotalSteps"], inputs["TotalDistance"])
        st.write(step_msg)
        st.write(distance_msg)

    except Exception as e:
        st.error(f"Prediction failed: {e}")
