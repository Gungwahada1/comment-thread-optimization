import json

# Function to load comments from a JSON file
def load_comments(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to optimize comments selection
def optimize_comments(thread, depth_limit):
    def dfs(comment, depth):
        """
        Depth-First Search (DFS) to traverse the comment tree and select comments.
        
        Args:
            comment (dict): The current comment node.
            depth (int): The current depth of traversal.
        
        Returns:
            tuple: Total engagement score and selected comment IDs.
        """
        # If depth exceeds the limit, discard this comment
        if depth > depth_limit:
            return 0, []
        
        # Initialize selected score and comment list
        selected_score = comment["score"]
        selected_comments = [comment["id"]]
        
        # Recursively process child comments
        for child in comment.get("children", []):
            child_score, child_comments = dfs(child, depth + 1)
            selected_score += child_score  # Accumulate engagement score
            selected_comments.extend(child_comments)  # Add selected child comments
        
        return selected_score, selected_comments
    
    # Start DFS from the root comment at depth 1
    _, result = dfs(thread, 1)
    return result

# Main function to execute the program
def main():
    comments_data = load_comments("comments.json")  # Load comments from file
    depth_limit = 10  # Set the maximum depth limit
    optimal_ids = optimize_comments(comments_data, depth_limit)  # Optimize comments
    print(optimal_ids)  # Print the selected comment IDs

# Entry point of the script
if __name__ == "__main__":
    main()