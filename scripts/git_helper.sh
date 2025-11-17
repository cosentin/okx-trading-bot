#!/bin/bash
echo "🚀 Git Helper for Trading Bot"

case $1 in
    "update")
        echo "📥 Updating bot from GitHub..."
        git pull origin main
        pip install -r requirements.txt
        ;;
    "commit")
        echo "📝 Committing changes..."
        git add .
        git commit -m "$2"
        ;;
    "push")
        echo "📤 Pushing to GitHub..."
        git push origin main
        ;;
    "status")
        echo "📊 Git Status:"
        git status
        ;;
    *)
        echo "Usage:"
        echo "  ./git_helper.sh update     - Update from GitHub"
        echo "  ./git_helper.sh commit \"msg\" - Commit changes"
        echo "  ./git_helper.sh push       - Push to GitHub"
        echo "  ./git_helper.sh status     - Check status"
        ;;
esac
