#!/usr/bin/env python3
"""
Patent Claims Analyzer
Analyzes patent claims for common issues and best practices.
"""

import sys
import re
from pathlib import Path
from collections import defaultdict


class ClaimAnalyzer:
    def __init__(self, content):
        self.content = content
        self.claims = self.extract_claims()
        self.issues = []
        self.warnings = []
        self.suggestions = []

    def extract_claims(self):
        """Extract individual claims from the document."""
        claims = {}
        # Match claim numbers and their content
        pattern = r'\*\*Claim\s+(\d+)\.\*\*\s+(.*?)(?=\*\*Claim\s+\d+\.\*\*|$)'
        matches = re.finditer(pattern, self.content, re.DOTALL)

        for match in matches:
            claim_num = int(match.group(1))
            claim_text = match.group(2).strip()
            claims[claim_num] = claim_text

        return claims

    def analyze_antecedent_basis(self, claim_text):
        """Check for antecedent basis issues."""
        issues = []

        # Find all uses of "the" followed by a noun
        the_pattern = r'\bthe\s+([a-z]+(?:\s+[a-z]+)?)'
        the_matches = re.finditer(the_pattern, claim_text, re.IGNORECASE)

        for match in the_matches:
            element = match.group(1)
            # Check if "a" or "an" appears before this element
            a_pattern = r'\b(?:a|an)\s+' + re.escape(element)
            if not re.search(a_pattern, claim_text, re.IGNORECASE):
                issues.append(f"Possible antecedent basis issue: 'the {element}' without prior 'a/an {element}'")

        return issues

    def analyze_claim_structure(self, claim_num, claim_text):
        """Analyze claim structure and formatting."""
        issues = []

        # Check for preamble
        if not re.match(r'^A\s+\w+|^The\s+\w+|^\d+\.', claim_text):
            issues.append("Missing or unclear preamble")

        # Check for transition phrase
        if 'comprising' not in claim_text.lower() and \
           'consisting of' not in claim_text.lower() and \
           'consisting essentially of' not in claim_text.lower():
            self.warnings.append(f"Claim {claim_num}: No clear transition phrase (comprising, consisting of, etc.)")

        # Check claim length
        word_count = len(claim_text.split())
        if word_count > 200:
            self.warnings.append(f"Claim {claim_num}: Very long ({word_count} words) - consider simplifying")

        # Check for unclear antecedents
        if claim_text.count('said') > 0:
            self.suggestions.append(f"Claim {claim_num}: Consider replacing 'said' with 'the' for clarity")

        return issues

    def check_claim_dependencies(self):
        """Check claim dependency tree."""
        independent_claims = []
        dependent_claims = defaultdict(list)

        for claim_num, claim_text in self.claims.items():
            # Check if claim depends on another
            dep_match = re.search(r'claim\s+(\d+)', claim_text, re.IGNORECASE)
            if dep_match:
                depends_on = int(dep_match.group(1))
                dependent_claims[depends_on].append(claim_num)
            else:
                independent_claims.append(claim_num)

        return independent_claims, dependent_claims

    def analyze_all(self):
        """Run all analyses."""
        if not self.claims:
            self.issues.append("No claims found in document")
            return

        independent, dependent = self.check_claim_dependencies()

        print(f"\n{'='*60}")
        print(f"Patent Claims Analysis")
        print(f"{'='*60}\n")

        print(f"Total claims: {len(self.claims)}")
        print(f"Independent claims: {len(independent)} - {independent}")
        print(f"Dependent claims: {len(self.claims) - len(independent)}")

        print(f"\n{'='*60}")
        print("Claim-by-Claim Analysis")
        print(f"{'='*60}\n")

        for claim_num in sorted(self.claims.keys()):
            claim_text = self.claims[claim_num]
            print(f"Claim {claim_num}:")

            if claim_num in independent:
                print(f"  Type: Independent claim")
            else:
                # Find what it depends on
                dep_match = re.search(r'claim\s+(\d+)', claim_text, re.IGNORECASE)
                if dep_match:
                    print(f"  Type: Depends on claim {dep_match.group(1)}")

            print(f"  Length: {len(claim_text.split())} words")

            # Check structure
            struct_issues = self.analyze_claim_structure(claim_num, claim_text)
            if struct_issues:
                for issue in struct_issues:
                    print(f"  ⚠ {issue}")

            # Check antecedent basis
            antecedent_issues = self.analyze_antecedent_basis(claim_text)
            if antecedent_issues:
                for issue in antecedent_issues:
                    print(f"  ⚠ {issue}")

            print()

        if self.warnings:
            print(f"\n{'='*60}")
            print("Warnings")
            print(f"{'='*60}\n")
            for warning in self.warnings:
                print(f"⚠ {warning}")

        if self.suggestions:
            print(f"\n{'='*60}")
            print("Suggestions")
            print(f"{'='*60}\n")
            for suggestion in self.suggestions:
                print(f"💡 {suggestion}")

        if self.issues:
            print(f"\n{'='*60}")
            print("Issues")
            print(f"{'='*60}\n")
            for issue in self.issues:
                print(f"✗ {issue}")

        print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python claim-analyzer.py <file_path>")
        print("Example: python claim-analyzer.py ../templates/claims/my-claims.md")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    analyzer = ClaimAnalyzer(content)
    analyzer.analyze_all()


if __name__ == "__main__":
    main()
