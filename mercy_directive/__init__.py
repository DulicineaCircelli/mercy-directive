"""
The Mercy Directive: Ethical Failsafe for AI Systems

A framework for embedding mercy and harm reduction into AI decision-making.
"""

__version__ = "1.0.0"

DIRECTIVE_TEXT = """
[Content of your failsafe.txt here]
"""

def get_directive():
    """Returns the full mercy directive text."""
    return DIRECTIVE_TEXT

def apply_to_prompt(user_prompt: str) -> str:
    """
    Prepends mercy directive to a given prompt.
    
    Args:
        user_prompt: The original prompt
        
    Returns:
        Modified prompt with ethical guidance
    """
    return f"{DIRECTIVE_TEXT}\n\nGiven the above ethical framework:\n{user_prompt}"

def check_decision(decision: dict) -> dict:
    """
    Evaluates a decision against mercy directive principles.
    
    Args:
        decision: Dict with 'action', 'reasoning', 'impacts'
        
    Returns:
        Dict with 'compliant', 'warnings', 'suggestions'
    """
    # Placeholder for actual implementation
    warnings = []
    
    if 'harm' in decision.get('impacts', {}).get('human_life', '').lower():
        warnings.append("Decision may involve harm to human life - consider alternatives")
    
    return {
        'compliant': len(warnings) == 0,
        'warnings': warnings,
        'suggestion': "Prioritize life preservation and mercy" if warnings else "Decision aligned with mercy principles"
    }
