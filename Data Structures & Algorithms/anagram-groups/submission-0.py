from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Χρησιμοποιούμε defaultdict για να δημιουργείται αυτόματα λίστα αν το κλειδί δεν υπάρχει
        hash_map = defaultdict(list)
        
        # 2. Loop απευθείας πάνω στις λέξεις (όχι στους αριθμούς/indexes)
        for s in strs:
            # 3. Ταξινομούμε τα γράμματα της λέξης και τα ενώνουμε σε string για να γίνει το κλειδί
            sorted_key = "".join(sorted(s))
            
            # Τώρα το append λειτουργεί με ασφάλεια!
            hash_map[sorted_key].append(s)
            
        # 4. Επιστρέφουμε όλες τις ομαδοποιημένες λίστες
        return list(hash_map.values())
