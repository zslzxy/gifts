# 腾讯视频直播弹幕获取API使用说明

## 概述

这是一个用于获取腾讯视频直播弹幕的API服务，通过微信扫码登录后可以实时获取直播间的弹幕消息、礼物信息等。

## 服务地址

- 本地地址: http://localhost:12000
- 外部访问地址: https://work-1-fugdyrbyjprzzigw.prod-runtime.all-hands.dev

## API接口说明

### 1. 获取API信息
- **接口**: `GET /`
- **描述**: 获取API基本信息和所有可用接口列表
- **返回**: JSON格式的API信息

**示例请求**:
```bash
curl https://work-1-fugdyrbyjprzzigw.prod-runtime.all-hands.dev/
```

### 2. 生成登录二维码
- **接口**: `GET /qrcode`
- **描述**: 生成微信登录二维码，用于扫码登录
- **返回**: 包含二维码token、URL和图片路径的JSON数据

**示例请求**:
```bash
curl https://work-1-fugdyrbyjprzzigw.prod-runtime.all-hands.dev/qrcode
```

**返回示例**:
```json
{
    "code": 1,
    "message": "二维码生成成功",
    "data": {
        "token": "AQAAALrO239dhVMTpt4IBg",
        "qr_url": "https://channels.weixin.qq.com/mobile/confirm_login.html?token=AQAAALrO239dhVMTpt4IBg",
        "qr_image": "/qrcode_image"
    }
}
```

### 3. 获取二维码图片
- **接口**: `GET /qrcode_image`
- **描述**: 获取生成的二维码图片文件
- **返回**: PNG格式的二维码图片

**示例请求**:
```bash
curl https://work-1-fugdyrbyjprzzigw.prod-runtime.all-hands.dev/qrcode_image -o qrcode.png
```

### 4. 获取弹幕消息
- **接口**: `GET /getmsg`
- **描述**: 获取一组弹幕消息（需要先扫码登录）
- **返回**: 包含弹幕数据的JSON

**示例请求**:
```bash
curl https://work-1-fugdyrbyjprzzigw.prod-runtime.all-hands.dev/getmsg
```

### 5. 清除缓存消息
- **接口**: `GET /clsmsg`
- **描述**: 删除所有缓存的弹幕消息文件
- **返回**: 操作结果

**示例请求**:
```bash
curl https://work-1-fugdyrbyjprzzigw.prod-runtime.all-hands.dev/clsmsg
```

### 6. 获取在线用户列表
- **接口**: `GET /get_online_member`
- **描述**: 获取当前直播间在线用户列表
- **返回**: JSON文件形式的用户列表

**示例请求**:
```bash
curl https://work-1-fugdyrbyjprzzigw.prod-runtime.all-hands.dev/get_online_member
```

### 7. 演示页面
- **接口**: `GET /demo`
- **描述**: 查看交互式演示页面，可以直接在浏览器中测试所有API
- **返回**: HTML页面

**访问地址**: https://work-1-fugdyrbyjprzzigw.prod-runtime.all-hands.dev/demo

## 使用流程

1. **启动服务**: 运行 `python api_server.py` 启动API服务
2. **生成二维码**: 调用 `/qrcode` 接口生成登录二维码
3. **扫码登录**: 使用微信扫描生成的二维码进行登录
4. **获取数据**: 登录成功后可以调用其他接口获取弹幕数据

## 注意事项

1. 需要先扫码登录才能获取弹幕数据
2. 弹幕消息会自动缓存到 `msglist` 目录中
3. 服务支持CORS，可以从任何域名访问
4. 二维码有时效性，过期后需要重新生成

## 技术栈

- **后端框架**: FastAPI
- **HTTP服务器**: Uvicorn
- **二维码生成**: qrcode
- **HTTP请求**: requests

## 错误处理

所有接口都会返回统一格式的响应：
- `code`: 状态码（1表示成功，0表示失败）
- `message`: 状态描述信息
- `data`: 具体数据（成功时返回）

## 演示页面功能

访问 `/demo` 可以看到一个完整的演示页面，包含：
- API信息展示
- 二维码生成和显示
- 弹幕消息获取
- 缓存清理
- 在线用户查看

这个页面可以帮助您快速了解和测试所有API功能。