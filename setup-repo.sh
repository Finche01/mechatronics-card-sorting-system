#!/bin/bash
# Automated Card Sorter - Repository Setup Script
# Run this after cloning your new GitHub repository

echo "=========================================="
echo "Automated Card Sorter - Repository Setup"
echo "=========================================="
echo ""

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ ERROR: Not in a git repository!"
    echo "Please run this script from your cloned repository directory."
    exit 1
fi

echo "✅ Git repository detected"
echo ""

# Extract the archive
echo "📦 Extracting repository files..."
if [ -f "automated-card-sorter-repo.tar.gz" ]; then
    tar -xzf automated-card-sorter-repo.tar.gz
    echo "✅ Files extracted successfully"
else
    echo "❌ ERROR: automated-card-sorter-repo.tar.gz not found!"
    echo "Please download it from Claude and place it in this directory."
    exit 1
fi

# Create necessary directories
echo ""
echo "📁 Creating directory structure..."
mkdir -p software/vision/templates/ranks
mkdir -p software/vision/templates/suits
mkdir -p software/vision/logs
mkdir -p software/node-red
mkdir -p software/plc/click-program
mkdir -p hardware/mechanical/nx-models
mkdir -p hardware/electrical/eplan-diagrams
mkdir -p tests
mkdir -p docs/images

echo "✅ Directory structure created"

# Set up git ignores
echo ""
echo "🔧 Configuring git..."
git config core.autocrlf input
echo "✅ Git configured"

echo ""
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "📝 Next steps:"
echo "1. Add your actual Python vision code to software/vision/"
echo "2. Add your Node-RED flows to software/node-red/"
echo "3. Add your PLC programs to software/plc/"
echo "4. Add your CAD files to hardware/mechanical/"
echo "5. Add system photos to docs/images/"
echo "6. Update the BOM Excel file in hardware/"
echo ""
echo "Then commit and push:"
echo "  git add ."
echo "  git commit -m \"Initial commit with complete project structure\""
echo "  git push origin main"
echo ""
echo "🌟 Your repository is ready to go!"
