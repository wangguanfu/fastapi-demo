### 一、Django框架的特点

Python 界最全能的 Web 开发框架，battery-include 各种功能完备，可维护性和开发速度一级棒。常有人说 Django 慢，其实主要慢在 Django ORM 与数据库的交互上，所以是否选用 Django，取决于项目对数据库交互的要求以及各种优化。而对于 Django 的同步特性导致吞吐量小的问题，其实可以通过 Celery 等解决，倒不是一个根本问题。具体特性有：

1.  有完善的ORM关系映射
2.  有强大的路由映射功能
3.  有完善的视图模板的实现
4.  有健全的后台管理系统
5.  有强大的缓存支持

-   项目Github地址：https://github.com/django/django

-   文档地址: https://docs.djangoproject.com/

### 二、Flask框架的特点

Flask主要特点是小而轻，原生组件几乎为零， 三方提供的组件请参考Django，非常全面，属于短小精悍型框架。通常应用于小型应用和快速构建应用，其强大的三方库，足以支撑一个大型的Web应用。具体特性有：

1.  内置开发服务器和快速调试器
2.  集成支持单元测试
3.  RESTful可请求调度
4.  Jinja2模板
5.  支持安全cookie（客户端会话）
6.  符合WSGI 1.0，基于Unicode
7.  Flask文档内容全面，丰富，结构合理

-   项目Github地址：https://github.com/pallets/flask

-   文档地址：https://flask.palletsprojects.com/

### 三、FastAPI框架的特点

Django 和 Flask 都属于同步特性的框架，而FastAPI是一个高性能的异步框架。自带 Swagger 作为 API 文档，不用后续去内嵌 Swagger-UI，。关键特性有：

1.  **快速**：可与 **NodeJS** 和 **Go** 比肩的极高性能（归功于 Starlette 和 Pydantic）
2.  **高效编码**：提高功能开发速度约 200％ 至 300％
3.  **更少 bug**：减少约 40％ 的人为（开发者）导致错误
4.  **智能**：极佳的编辑器支持。处处皆可自动补全，减少调试时间
5.  **简单**：设计的易于使用和学习，阅读文档的时间更短
6.  **简短**：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少
7.  **健壮**：生产可用级别的代码。还有自动生成的交互式文档
8.  **标准化**：基于（并完全兼容）API 的相关开放标准：[OpenAPI](https://github.com/OAI/OpenAPI-Specification) (以前被称为 Swagger) 和 [JSON Schema](https://json-schema.org/)

-   项目Github地址：https://github.com/tiangolo/fastapi

-   文档地址：https://fastapi.tiangolo.com/

### 四、性能排名

可以看到，常用的 Python Web 框架里面，FastAPI遥遥领先。不过网上资料很少，多是 Django/Flask/Tornado 框架的对比，因为 FastAPI 是新秀。

![image-20210112151309652](./images/performance_benchmarks.png)

参考： https://www.techempower.com/benchmarks/#section=data-r19&hw=ph&test=fortune&f=zhb2t3-yyku7z-v2qiv3-zik0zj-zik0zj-zik0zj-zik0sf-ziimf3-zik0zj-zik0zj-73



