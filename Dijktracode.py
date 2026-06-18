import random
import heapq
import itertools

def generate_random_graph(nodes, p=0.7, q=0.3):
    """
    Δημιουργεί έναν τυχαίο γράφο σύμφωνα με τις πιθανότητες της άσκησης.
    Επιστρέφει τη δομή του γράφου (λίστα γειτνίασης) και ένα boolean 
    για το αν υπάρχουν αρνητικές ακμές.
    """
    adj = {node: [] for node in nodes}
    has_negative_edge = False
    
    # Βρίσκουμε όλα τα πιθανά ζεύγη κορυφών
    pairs = list(itertools.combinations(nodes, 2))
    
    for u, v in pairs:
        # Πιθανότητα p=0.7 να υπάρχει σύνδεση μεταξύ των δύο κορυφών
        if random.random() < p:
            has_negative_edge = True # Εφόσον τα βάρη είναι 1 και -1, σίγουρα θα υπάρχει αρνητική ακμή
            
            # Πιθανότητα q=0.3 η πρώτη κατεύθυνση να είναι -1 και η αντίθετη +1
            if random.random() < q:
                weight_uv, weight_vu = -1, 1
            else:
                weight_uv, weight_vu = 1, -1
                
            adj[u].append((v, weight_uv))
            adj[v].append((u, weight_vu))
            
    return adj, has_negative_edge

def dijkstra(graph, start):
    """
    Κλασική υλοποίηση Dijkstra. 
    Σημείωση: Αποφεύγουμε την επανεξέταση επισκεπτόμενων κόμβων 
    για να μην πέσει σε ατέρμονο βρόχο λόγω αρνητικών κύκλων.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        for v, weight in graph[u]:
            if current_dist + weight < distances[v]:
                distances[v] = current_dist + weight
                heapq.heappush(pq, (distances[v], v))
                
    return distances

def bellman_ford(graph, nodes, start):
    """
    Υλοποίηση Bellman-Ford που διαχειρίζεται αρνητικά βάρη 
    και ανιχνεύει αρνητικούς κύκλους.
    """
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0
    
    # Χαλάρωση (relaxation) ακμών |V| - 1 φορές
    for _ in range(len(nodes) - 1):
        for u in nodes:
            for v, weight in graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    
    # Έλεγχος για αρνητικό κύκλο στο (V)-οστο βήμα
    has_negative_cycle = False
    for u in nodes:
        for v, weight in graph[u]:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                has_negative_cycle = True
                break
        if has_negative_cycle:
            break
            
    return distances, has_negative_cycle

def run_simulation(num_trials=10000):
    nodes = ['s', 'A', 'B', 't']
    
    stats = {
        'total_graphs': num_trials,
        'with_negative_edges': 0,
        'with_negative_cycles': 0,
        'dijkstra_correct': 0,
        'dijkstra_incorrect': 0
    }
    
    print(f"Εκτέλεση προσομοίωσης για {num_trials} τυχαίους γράφους...\n")
    
    for _ in range(num_trials):
        # 1. Δημιουργία Γράφου
        graph, has_neg_edges = generate_random_graph(nodes, p=0.7, q=0.3)
        
        if has_neg_edges:
            stats['with_negative_edges'] += 1
            
        # 2. Εκτέλεση Dijkstra
        dijkstra_dists = dijkstra(graph, 's')
        
        # 3. Εκτέλεση Bellman-Ford
        bf_dists, has_neg_cycle = bellman_ford(graph, nodes, 's')
        
        # 4. Καταγραφή & Σύγκριση Αποτελεσμάτων
        if has_neg_cycle:
            stats['with_negative_cycles'] += 1
            # Αν υπάρχει αρνητικός κύκλος, ο Dijkstra εξ' ορισμού δίνει λάθος 
            # αποτέλεσμα (βγάζει πεπερασμένη απόσταση ενώ είναι -άπειρο)
            stats['dijkstra_incorrect'] += 1
        else:
            # Αν ΔΕΝ υπάρχει αρνητικός κύκλος, ελέγχουμε αν οι αποστάσεις ταυτίζονται
            if dijkstra_dists == bf_dists:
                stats['dijkstra_correct'] += 1
            else:
                stats['dijkstra_incorrect'] += 1
                
    # Εμφάνιση Αποτελεσμάτων
    print("=" * 50)
    print(" ΣΤΑΤΙΣΤΙΚΑ ΑΠΟΤΕΛΕΣΜΑΤΑ ΠΡΟΣΟΜΟΙΩΣΗΣ")
    print("=" * 50)
    print(f"Συνολικοί Γράφοι που ελέγχθηκαν     : {stats['total_graphs']}")
    print(f"Γράφοι με Αρνητικές Ακμές           : {stats['with_negative_edges']}")
    print(f"Γράφοι με Αρνητικούς Κύκλους        : {stats['with_negative_cycles']}")
    print("-" * 50)
    print(f"Περιπτώσεις που ο Dijkstra ήταν ΣΩΣΤΟΣ  : {stats['dijkstra_correct']} "
          f"({(stats['dijkstra_correct']/num_trials)*100:.2f}%)")
    print(f"Περιπτώσεις που ο Dijkstra ήταν ΛΑΘΟΣ   : {stats['dijkstra_incorrect']} "
          f"({(stats['dijkstra_incorrect']/num_trials)*100:.2f}%)")
    print("=" * 50)

if __name__ == "__main__":
    run_simulation(10000)