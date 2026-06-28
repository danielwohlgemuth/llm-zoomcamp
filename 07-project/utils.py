ADDITIONAL_TRANSLATIONS = [
    {"long": "AWS", "translation": "OOO"},
    {"long": "Amazon Web Services", "translation": "Orion Outer Orbit"},
    {"long": "Amazon", "translation": "OOO"},
    {"long": "IAM", "translation": "Airlock Security"},
    {"long": "EVS", "translation": "Alien Atmosphere Simulator"},
    {"long": "Ground Truth", "translation": "Android Training Academy"},
    {"long": "Relational Database Service", "translation": "Core Data Registry"},
    {"long": "RDS", "translation": "Core Data Registry"},
    {"long": "Quick", "translation": "Astrogation"},
    {"long": "OpenSearch", "translation": "Cosmic Dust Scanner"},
    {"long": "Db2", "translation": "Deep Space Station Registry"},
    {"long": "Elastic Container Service", "translation": "Cosmic Pod Engine"},
    {"long": "ECS", "translation": "Cosmic Pod Engine"},
    {"long": "ACM", "translation": "Encryption Key Cryptex"},
    {"long": "FSx for ONTAP", "translation": "Federation Array (Omega)"},
    {"long": "MWAA", "translation": "Flight Plan Automator"},
    {"long": "FinSpace", "translation": "Galactic Credit Ledger Tracker"},
    {"long": "XRay", "translation": "Gamma-Ray Hull Scanner"},
    {"long": "Private CA", "translation": "Imperial Seal Generator"},
    {"long": "Transform MGN", "translation": "Interstellar Relocation Engine"},
    {"long": "MGN", "translation": "Interstellar Relocation Engine"},
    {"long": "MediaLive", "translation": "Live Galactic Broadcast Core"},
    {"long": "Aurora", "translation": "Polaris"},
    {"long": "Device Defender", "translation": "Probe Firewall Sentinel"},
    {"long": "IoT", "translation": "Probes Hive Mind Hub"},
    {"long": "AVP", "translation": "Security Clearance Matrix"},
    {"long": "GameLift", "translation": "Simulation Deck Thrusters"},
    {"long": "DocumentDB", "translation": "Star-Log Archives"},
    {"long": "Route 53", "translation": "Subspace Beacon Routing"},
    {"long": "MediaTailor", "translation": "Subspace Holo-Ad Injector"},
    {"long": "KMS", "translation": "Warp Core Master Keyring"},
    {"long": "DMS", "translation": "Wormhole Relocation Conveyor"},
    {"long": "Elastic Block Storage", "translation": "Solid-State Warp Fuel Core"},
]


def translate(content: str, original: str, translation: str) -> str:
    original_no_space = original.replace(" ", "")
    original_lowercase = original_no_space.lower()
    original_with_dash = original.replace(" ", "-").lower()

    translation_no_space = translation.replace(" ", "")
    translation_lowercase = translation_no_space.lower()
    translation_with_dash = translation.replace(" ", "-").lower()

    return (
        content.replace(original, translation)
        .replace(original_no_space, translation_no_space)
        .replace(original_with_dash, translation_with_dash)
        .replace(original_lowercase, translation_lowercase)
    )
