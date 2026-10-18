"""Bind managed reviewed profiles to their exact packet and editorial attestation."""
import hashlib
import json


def check_managed_reviews(root, documents):
    count = 0
    for doc in documents:
        ticker = doc.metadata["ticker"]
        packet = root / "research/pilot" / (ticker + ".json")
        if not packet.exists():
            packet = root / "research/evidence" / (ticker + ".json")
        if doc.metadata["status"] != "reviewed" or not packet.exists():
            continue
        path = root / "research/reviews" / (ticker + ".json")
        if not path.exists():
            raise ValueError(f"{ticker}: reviewed managed profile has no review record")
        record = json.loads(path.read_text())
        if record.get("packet_path") != packet.relative_to(root).as_posix() or record.get("profile_path") != doc.path.relative_to(root).as_posix():
            raise ValueError(f"{ticker}: review record points to another profile or packet")
        expected = hashlib.sha256(doc.path.read_bytes()).hexdigest()
        packet_hash = hashlib.sha256(packet.read_bytes()).hexdigest()
        if record.get("approved_profile_sha256") != expected or record.get("packet_sha256") != packet_hash:
            raise ValueError(f"{ticker}: profile or evidence changed after review; return it to draft and review again")
        if record.get("reviewed_at") != doc.metadata["reviewed_at"]:
            raise ValueError(f"{ticker}: review date differs from attestation")
        count += 1
    return count
