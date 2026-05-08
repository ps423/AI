# AI Slips Execution Helper Script
import os
import sys

def main():
    print("=" * 50)
    print("    AI Slips Execution Helper")
    print("=" * 50)
    print()
    print("Usage: python run_slip.py <slip_number> <question_number>")
    print()
    print("Examples:")
    print("  python run_slip.py 1 1    # Run Slip1 Q1")
    print("  python run_slip.py 5 2    # Run Slip5 Q2")
    print("  python run_slip.py all    # Run all programs")
    print()
    
    if len(sys.argv) < 2:
        print("Please specify slip number and question number")
        return
    
    if sys.argv[1] == "all":
        print("Running all programs...")
        for slip_num in range(1, 26):
            slip_dir = f"Slip{slip_num}"
            if os.path.exists(slip_dir):
                print(f"\n--- {slip_dir} ---")
                for q_num in [1, 2]:
                    q_file = os.path.join(slip_dir, f"Q{q_num}.py")
                    if os.path.exists(q_file):
                        print(f"\nRunning Q{q_num}...")
                        try:
                            exec(open(q_file).read())
                        except Exception as e:
                            print(f"Error running {q_file}: {e}")
        return
    
    slip_num = sys.argv[1]
    if len(sys.argv) < 3:
        print("Please specify question number (1 or 2)")
        return
    
    q_num = sys.argv[2]
    slip_dir = f"Slip{slip_num}"
    q_file = os.path.join(slip_dir, f"Q{q_num}.py")
    
    if not os.path.exists(slip_dir):
        print(f"Slip{slip_num} does not exist!")
        return
    
    if not os.path.exists(q_file):
        print(f"Q{q_num}.py not found in {slip_dir}!")
        return
    
    print(f"Running {slip_dir}/Q{q_num}.py...")
    try:
        exec(open(q_file).read())
    except Exception as e:
        print(f"Error running program: {e}")

if __name__ == "__main__":
    main()
