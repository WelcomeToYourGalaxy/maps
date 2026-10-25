"""This map's own count of World Bank policy-loan conditions, from the agreement texts
extracted by Winter, Cormier, Kramarz and Manger (2025).

Rule, applied the same way to every text:
 1. Find the list of required actions by its heading, written as a heading (capital letters):
    "Actions Taken ...", "Actions Referred to in ...", "Actions to be Taken ...", "Program
    Actions", "Prior Actions", "Conditions for/of Release", "Tranche Release Conditions",
    "Release of the Second/Third Tranche", skipping any that is followed by a list of
    definitions ("... means ...").
 2. Read from there to the end of that section: the next "////" break in the extracted text,
    or the next schedule (repayment or procurement), whichever comes first.
 3. Count the list items: numbered items ("1. Establish ...") and lettered items ("(a) ...").
    Whichever of the two gives more is the count (one list is usually nested inside groups of the other).
 4. A text with no such heading gets no count.
"""
import re
HEAD = re.compile(r"Actions? (?:Taken|taken|Referred|referred|to be [Tt]aken|Undertaken|undertaken)(?! are)|Program Actions|Prior Actions|Conditions? (?:of|for) (?:the )?Release|Tranche Release Conditions|Release of the (?:Second|Third|Fourth|Final) Tranche")
DEFN = re.compile(r"['\u2019\u201d] means |\bmeans the\b", re.I)
NUM = re.compile(r"(?:^|[\s;:])(\d{1,2})\.\s+[A-Z(]")
LET = re.compile(r"(?:^|[\s;:])\(([a-z])\)\s")
def count(text):
    for m in HEAD.finditer(text):
        seg = text[m.start():]
        j = seg.find("////", 20)
        if j > 0: seg = seg[:j]
        k = re.search(r"SCHEDULE \d|Amortization Schedule|Procurement\s", seg[20:])
        if k: seg = seg[:20 + k.start()]
        if DEFN.search(seg[:600]):      # a definitions list, not a list of actions: look further on
            continue
        break
    else:
        return None
    nums = [int(x) for x in NUM.findall(seg)]
    # numbered items: count each item; a list restarting at 1 under a new group adds on
    n1 = len(nums)
    lets = LET.findall(seg)
    n2 = len(lets)
    return max(n1, n2) if max(n1, n2) > 0 else None
