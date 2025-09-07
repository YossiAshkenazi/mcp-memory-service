#!/usr/bin/env python3
"""Test script to verify MCP Memory Service installation."""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that required modules can be imported."""
    print("Testing imports...")
    
    try:
        import mcp_memory_service
        print(f"✓ mcp_memory_service imported (version: {mcp_memory_service.__version__})")
    except ImportError as e:
        print(f"✗ Failed to import mcp_memory_service: {e}")
        return False
    
    try:
        import sqlite_vec
        print("✓ sqlite_vec imported")
    except ImportError as e:
        print(f"✗ Failed to import sqlite_vec: {e}")
        return False
    
    try:
        import sentence_transformers
        print("✓ sentence_transformers imported")
    except ImportError as e:
        print(f"✗ Failed to import sentence_transformers: {e}")
        return False
    
    try:
        import torch
        print(f"✓ torch imported (version: {torch.__version__})")
    except ImportError as e:
        print(f"✗ Failed to import torch: {e}")
        return False
    
    try:
        import fastapi
        print("✓ fastapi imported")
    except ImportError as e:
        print(f"✗ Failed to import fastapi: {e}")
        return False
    
    try:
        import mcp
        print("✓ mcp imported")
    except ImportError as e:
        print(f"✗ Failed to import mcp: {e}")
        return False
    
    return True

def test_sqlite_backend():
    """Test SQLite-vec backend initialization."""
    print("\nTesting SQLite-vec backend...")
    
    try:
        from mcp_memory_service.storage.backends.sqlite_vec_backend import SQLiteVecBackend
        
        # Try to initialize the backend
        backend = SQLiteVecBackend(db_path=":memory:")
        print("✓ SQLite-vec backend initialized successfully")
        
        # Test basic operations
        backend.store(
            content="Test memory content",
            metadata={"source": "test_script"}
        )
        print("✓ Successfully stored test memory")
        
        results = backend.search("test", limit=1)
        if results:
            print("✓ Successfully searched memories")
        
        backend.close()
        return True
        
    except Exception as e:
        print(f"✗ Failed to test SQLite-vec backend: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 50)
    print("MCP Memory Service Setup Test")
    print("=" * 50)
    
    # Set environment variable for SQLite backend
    os.environ["MCP_MEMORY_STORAGE_BACKEND"] = "sqlite_vec"
    
    all_passed = True
    
    if not test_imports():
        all_passed = False
    
    if not test_sqlite_backend():
        all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✓ All tests passed! The service is ready to use.")
        print("\nNext steps:")
        print("1. Start the server: uv run memory server")
        print("2. Configure Claude Desktop integration")
    else:
        print("✗ Some tests failed. Please check the errors above.")
    print("=" * 50)

if __name__ == "__main__":
    main()