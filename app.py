from rapidfuzz import fuzz
import json

# Define intent keywords BEFORE functions that use it
intent_keywords = {
    "admissions": ["admission", "enroll", "application", "apply", "register", "requirements"],
    "school events": ["careerday", "interhousesport", "graduation", "seminar", "excursion", "ceremony"],
    "fees and payments": ["fees", "payment", "pay", "tuition", "school fees", "invoice"],
    "contact": ["contact", "call", "email", "reach", "address", "location"],
    "school staff": ["principal", "teacher", "admin", "staff", "coordinator", "head"],
    "academics": ["exam", "timetable", "schedule", "classes", "subjects", "curriculum", "results"],
    "support": ["help", "support", "question", "assist", "guide", "info"],
}

# Normalize synonyms
def normalize_input(text):
    synonyms = {
        "liberate academy": "school",
        "liberate school": "school",
        "la": "school",
        "lib academy": "school",
        "lib school": "school",
        "liberat academy": "school",
        "liberat school": "school",
        "libarate academy": "school",
        "libarate school": "school",
        "liberete academy": "school",
        "liberate acdemy": "school",
        "the academy": "school",
        "academy": "school"
    }
    text = text.lower()
    for key, replacement in synonyms.items():
        text = text.replace(key, replacement)
    return text

def smart_redirect(user_input):
    user_input = user_input.lower()
    support_numbers = ["08100987608", "08035638671"]
    support_info = " or ".join(support_numbers)
    school_address = "Emesiri Street Off Sokoh Estate Road, Warri, Nigeria"

    if any(word in user_input for word in intent_keywords["admissions"]):
        return f"📘 For admission or registration enquiries, please call our admin office at {support_info}."

    if any(word in user_input for word in intent_keywords["school events"]):
        return f"📅 Want to know about events like Career Day or Inter-house Sports? Please call {support_info} for details."

    if any(word in user_input for word in intent_keywords["fees and payments"]):
        return (
            "💳 Here are our payment details:\n"
            "**Bank Name:** EcoBank\n"
            "**Account Name:** Liberate Academy\n"
            "**Account Number:** 123456789\n\n"
            f"For confirmation or questions about payments, call {support_info}."
        )

    if "address" in user_input or "location" in user_input:
        return f"🏫 Our school is located at: {school_address}. You can also call us at {support_info}."

    if any(word in user_input for word in intent_keywords["contact"]):
        return f"📞 You can reach us directly at {support_info}. The school address is: {school_address}."

    if any(word in user_input for word in intent_keywords["school staff"]):
        return f"👩‍🏫 For staff-related enquiries, like speaking with a teacher or the principal, call {support_info}."

    if any(word in user_input for word in intent_keywords["academics"]):
        return f"📚 For information on exams, timetables, or results, please call {support_info}."

    if any(word in user_input for word in intent_keywords["support"]):
        return f"❓Need help with anything? Our support team is available at {support_info}."

    return None  # Let get_response handle fallback

def get_response(user_input):
    normalized_input = normalize_input(user_input)

    # First, check smart redirect
    smart_reply = smart_redirect(normalized_input)
    if smart_reply:
        return smart_reply

    # Then fallback to response.json matching
    try:
        with open("responses.json", "r") as file:
            responses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return "⚠️ Sorry, I can't find my response data."

    best_match = None
    highest_score = 0

    for keyword, reply in responses.items():
        score = fuzz.partial_ratio(normalized_input.lower(), keyword.lower())
        if score > highest_score:
            highest_score = score
            best_match = reply

    if highest_score > 80:
        return best_match

    return "🤖 I’m not sure I understood that. Please call 08100987608 or 08035638671 for assistance."

__all__ = ['get_response']

    
