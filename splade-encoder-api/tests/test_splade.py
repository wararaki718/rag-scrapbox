import json
from splade_encoder_api.encoder import SpladeEncoder


def test_encode():
    print("Initializing encoder...")
    encoder = SpladeEncoder(model_id="hotchpotch/japanese-splade-v2")
    
    text = "Scrapboxは知識を共有するためのツールです。"
    print(f"Encoding text: {text}")
    
    sparse_vector = encoder.encode(text)
    assert len(sparse_vector) > 0
    
    tokens_with_weights = encoder.get_tokens_and_weights(sparse_vector)
    # Check if some relevant Japanese tokens or related concepts are present
    assert len(tokens_with_weights) > 0
    
    print("\nSparse Vector (first 5 elements):")
    # Sort by weight descending
    sorted_tokens = sorted(tokens_with_weights.items(), key=lambda x: x[1], reverse=True)
    for token, weight in sorted_tokens[:10]:
        print(f"  {token}: {weight:.4f}")
    
    print(f"\nTotal non-zero dimensions: {len(sparse_vector)}")

if __name__ == "__main__":
    test_encode()
