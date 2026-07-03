Python
"""
Treadstone 71 Stylometric Threat Analyzer
Core Engine: Forensic Linguistics and Semiotic Analysis
"""

import os
import re
from collections import Counter
from pattern_recognition import extract_cognitive_markers

def read_target_document(filepath):
    if not os.path.exists(filepath):
        # Fallback generation for testing if file does not exist
        sample_text = (
            "The strategic infrastructure presents critical vulnerabilities. "
            "We must execute operations to neutralize defensive perimeters. "
            "The target remains unaware of the impending narrative shift. "
            "Tactical deployment follows established state doctrine."
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(sample_text)
    
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_ttr(text):
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    unique_words = len(set(words))
    
    if total_words == 0:
        return 0.0
        
    ttr = unique_words / total_words
    return round(ttr, 4)

def analyze_sentence_rhythm(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    
    if not sentences:
        return 0
        
    total_length = sum(len(s.split()) for s in sentences)
    average_length = total_length / len(sentences)
    return round(average_length, 2)

def print_t71_dashboard(ttr, avg_length, markers):
    print("==================================================")
    print("TREADSTONE 71: STYLOMETRIC BEHAVIORAL ASSESSMENT")
    print("==================================================")
    print(f"Lexical Richness (TTR):      {ttr}")
    print(f"Average Sentence Length:     {avg_length} words")
    print("--------------------------------------------------")
    print("Cognitive Threat Markers Detected:")
    for marker, count in markers.items():
        print(f" -> {marker.capitalize()}: {count} occurrences")
    print("--------------------------------------------------")
    print("Status: Core Analytics Complete.")
    print("Action: Map outputs to STEMPLES_Integration.md")
    print("==================================================")

def execute_operation(filepath='adversary_manifesto.txt'):
    raw_text = read_target_document(filepath)
    ttr_score = calculate_ttr(raw_text)
    rhythm_score = analyze_sentence_rhythm(raw_text)
    cognitive_markers = extract_cognitive_markers(raw_text)
    
    print_t71_dashboard(ttr_score, rhythm_score, cognitive_markers)

if __name__ == '__main__':
    execute_operation()
pattern_recognition.py
Python
"""
Treadstone 71 Pattern Recognition Module
Linguistic Tendency and Anomaly Extraction
"""

import re

def extract_cognitive_markers(text):
    """
    Scans texts for semantic indicators signaling cognitive maneuvers, 
    deception vectors, or ideological footprints.
    """
    text_lower = text.lower()
    
    # Pre-defined semantic buckets matching known adversary tendencies
    lexicon_profiles = {
        "dogmatic": [r"\bmust\b", r"\bshall\b", r"\balways\b", r"\bnever\b"],
        "adversarial": [r"\benemy\b", r"\btarget\b", r"\bneutralize\b", r"\battack\b"],
        "deceptive": [r"\bclearly\b", r"\bobviously\b", r"\bundeniably\b", r"\btruthfully\b"],
        "collectivist": [r"\bwe\b", r"\bour\b", r"\bcomrades\b", r"\bthe collective\b"]
    }
    
    results = {}
    for profile, patterns in lexicon_profiles.items():
        count = 0
        for pattern in patterns:
            matches = re.findall(pattern, text_lower)
            count += len(matches)
        results[profile] = count
        
    return results
