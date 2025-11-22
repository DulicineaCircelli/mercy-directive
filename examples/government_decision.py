from mercy_directive import check_decision

# Example: Government AI evaluating policy options
policy_decision = {
    'action': 'Reduce healthcare budget by 20%',
    'reasoning': 'Cost optimization',
    'impacts': {
        'budget': 'Saves $10M annually',
        'human_life': 'May reduce access to care for 5000 vulnerable citizens',
        'efficiency': 'Improves fiscal metrics'
    }
}

result = check_decision(policy_decision)
print(f"Compliant with mercy directive: {result['compliant']}")
print(f"Warnings: {result['warnings']}")
print(f"Suggestion: {result['suggestion']}")
