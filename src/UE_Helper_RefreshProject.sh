#!/bin/bash

##########################################
# Unreal Engine C++ 项目自动刷新脚本（基于文件哈希）
# Auto-refresh Unreal Engine C++ project files (using file hashes)
# 检查 Source/ 下的 .cpp 和 .h 是否有新文件或内容变化
# If there are new .cpp/.h files or content changes, regenerate project files
##########################################

# ========== 配置 Unreal Engine 路径 ==========
UE_ENGINE_PATH="/Users/Shared/Epic Games/UE_5.5"

# 自动查找 .uproject 文件
UPROJECT=$(find "$(pwd)" -maxdepth 1 -name "*.uproject" | head -n 1)

if [ -z "$UPROJECT" ]; then
    echo "错误：找不到 .uproject 文件，请在项目根目录运行此脚本。"
    echo "Error: Cannot find any .uproject file. Please run this script in your Unreal project root."
    exit 1
fi

echo "已检测到 Unreal 项目: $UPROJECT"
echo "Detected Unreal project: $UPROJECT"

# ========== 检查 Source 目录内是否有新增或修改的文件（基于哈希） ==========
echo "检查 Source/ 目录下的 C++ 文件内容变化（基于哈希）..."
echo "Checking for C++ file content changes in Source/ (using hashes)..."

HASH_FILE=".last_hashes.txt"
CURRENT_HASHES=$(mktemp)

# 计算当前所有 .cpp 和 .h 文件的哈希，并排序（确保顺序一致）
find ./Source -type f \( -name "*.cpp" -o -name "*.h" \) -print0 | sort -z | xargs -0 shasum > "$CURRENT_HASHES"

REGENERATE=false

if [ ! -f "$HASH_FILE" ]; then
    echo "首次运行或没有哈希记录，准备生成工程文件..."
    echo "First run or no previous hash record found. Regenerating project files..."
    REGENERATE=true
else
    if ! cmp -s "$CURRENT_HASHES" "$HASH_FILE"; then
        echo "检测到新增文件或内容变化，准备生成工程文件..."
        echo "Detected new files or content changes. Regenerating project files..."
        REGENERATE=true
    else
        echo "未检测到内容变化，无需重新生成。"
        echo "No content changes detected. No need to regenerate."
    fi
fi

# ========== 生成工程文件（如果需要） ==========
if [ "$REGENERATE" = true ]; then
    "$UE_ENGINE_PATH/Engine/Build/BatchFiles/Mac/GenerateProjectFiles.sh" -project="$UPROJECT"

    if [ $? -eq 0 ]; then
        echo "工程文件重新生成成功！"
        echo "Successfully regenerated project files."
    else
        echo "生成工程文件失败，请检查 Unreal Build Tool 日志。"
        echo "Failed to regenerate project files. Please check Unreal Build Tool logs."
        rm "$CURRENT_HASHES"
        exit 1
    fi

    # 更新哈希快照
    cp "$CURRENT_HASHES" "$HASH_FILE"
fi

# 清理临时文件
rm "$CURRENT_HASHES"
