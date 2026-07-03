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
