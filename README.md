# LLM-Rabbit
## langchain依赖管理
1、安装自动化管理工具
```bash
pip install pip-tools
```
2、编辑requirements.in文件，添加主依赖
```text
# requirements.in
langchain==0.3.26
langchain-core==0.3.66
langchain-community==0.3.26
langchain-openai==0.3.27
langchain-text-splitters==0.3.8
```
3、编译生成requirements.txt
```bash
pip-compile requirements.in
```
4、在新环境下安装依赖
```bash
pip install -r requirements.txt
```

## 文档总结、精炼、翻译
1、安装依赖
```bash
pip install doctran
```