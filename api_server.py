#!/usr/bin/env python3
"""
简化的API服务器启动脚本
只启动FastAPI服务，不需要立即扫码登录
"""

import uvicorn
from webapi import app

if __name__ == '__main__':
    print("启动腾讯视频直播弹幕获取API服务...")
    print("服务将在 http://0.0.0.0:12000 启动")
    print("API接口说明:")
    print("  GET /              - API说明")
    print("  GET /qrcode        - 获取登录二维码")
    print("  GET /qrcode_image  - 获取二维码图片")
    print("  GET /getmsg        - 获取弹幕消息")
    print("  GET /clsmsg        - 清除所有缓存消息")
    print("  GET /get_online_member - 获取在线用户列表")
    print("\n按 Ctrl+C 停止服务")
    
    uvicorn.run(app, host="0.0.0.0", port=12000, reload=False)