# Projet 2 - Mini Firewall - Moubarak Gremah - Univ de Dosso
# Objectif : apprendre à bloquer une IP dangereuse
# Date : Octobre 2026 - Dosso

# Ma liste noire - IP que j'ai vu dans les TP réseau
liste_noire_dosso = ["192.168.1.100", "10.0.0.5", "192.168.1.1"]

def verifier_ip_dosso(adresse_ip):
    print(f"\n[Dosso] Je vérifie l'IP : {adresse_ip}")
    
    if adresse_ip in liste_noire_dosso:
        print(f"🚨 ATTENTION ! L'IP {adresse_ip} est bloquée !")
        print("-> C'est une IP de ma liste noire, je refuse la connexion.")
        print("-> Alerte envoyée à l'admin système de Dosso.")
        return False
    else:
        print(f"✅ IP {adresse_ip} c'est bon, je laisse passer.")
        return True

# Programme principal
print("=== MINI FIREWALL - UNIVERSITE DE DOSSO ===")
print("Petit outil pour apprendre la défense réseau")

# Test 1 : l'utilisateur entre une IP
ip_test = input("\nEntre une IP pour tester (ex: 8.8.8.8) : ")
verifier_ip_dosso(ip_test)

# Test 2 : je montre que ça bloque vraiment
print("\n--- Démonstration automatique ---")
verifier_ip_dosso("192.168.1.100") # Celle-ci doit être bloquée
verifier_ip_dosso("8.8.8.8") # Celle-ci c'est Google, elle est sûre

print("\nFin du programme. Projet 2 terminé.")