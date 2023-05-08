import openai
from dotenv import load_dotenv
import os
import sys


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")


def get_completion(prompt, model="gpt-3.5-turbo", stream=False):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.8,
        stream=stream,
    )
    if stream:
        collected_messages = []
        for chunk in response:
            chunk_message = chunk['choices'][0]['delta']  # extract the message
            if 'content' in chunk_message:
                content = chunk_message['content']
                collected_messages.append(content)
                print(content, end="", flush=True)
        return "".join(collected_messages)
    else:
        content = response.choices[0].message["content"]
        print(content, flush=True)
        return content


model = 'gpt-3.5-turbo'
stream = True
prompt = '''你是自然资源监测中心的主任，需要向浙江省测绘科学技术研究院纪委书记做工作报告，汇报的核心内容是监测中心如何落实全面从严治党“四责协同”机制。
请生成一份2000字的工作报告。我列出了“四责协同”的定义，浙江省测绘科学技术研究院的职责，以及自然资源监测中心的职责，供你参考，报告中不需要说明“四责协同”的定义、本院的职责以及本中心的职责。 

“四责协同” 
```
是指党委的主体责任，纪委的监督责任，党委书记的第一责任以及班子成员的一岗双责责任，这四个方面是互相促进和共同发展的。监测中心深入贯彻落实习近平总书记重要讲话、重要指示精神和党中央决策部署，坚持把该履行的责任没有履行是失责、责任落实各自为政也是失责的理念和要求贯穿责任履行全过程，对管党治党的责任主体、内容方式、环节过程等进行系统梳理与科学安排，明确党委主体责任是根本、纪委监督责任是保障、党委书记第一责任人责任是关键、班子成员“一岗双责”是支撑，推动四个责任主体齐心协力，共同干好分内事，推动管党治党同向发力、形成合力。
```

浙江省测绘科学技术研究院的主要职责是：
```
负责全省卫星导航定位基准服务系统建设管理、省级基础测绘成果和基础地理信息系统更新；负责数字浙江和智慧城市空间地理大数据建设、地理信息公共服务；承担全省自然资源所有者权益管理的技术工作，承担测绘对外交流合作和军民融合具体事务；承担全省国土卫星遥感应用和自然资源行政执法的技术工作，承担全省突发公共事件应急测绘保障服务；承担全省地图管理和国家版图意识教育的技术服务，承担全省综合、普通地图（集）编制工作，开展导航电子地图编制和互联网地图服务；承担全省测绘成果和档案资料管理及分发工作，承担测绘成果保密技术处理和公开出版地图的技术审查；负责测绘地理信息科技展览展示、科普教育及展品收藏和研究；提供测绘航空摄影、摄影测量与遥感、工程测量、不动产测绘、海洋测绘、三维实景数据建设、地理信息工程建设、自然资源调查监测的技术服务；承担全省测绘成果质量检验、鉴定及测绘器具检定工作，承担测绘发展规划、技术标准的研究和起草工作，开展测绘基础和应用研究、测绘科技项目攻关、测绘软件研发、测绘成果转化和科技咨询；完成浙江省自然资源厅交办的其他任务。
```

自然资源监测中心是浙江省测绘科学技术研究院的业务部门，它的主要职责是：
```
承担全省国土卫星遥感应用、自然资源所有者权益管理和自然资源行政执法技术支撑,负责省级重大规划、重点项目等实施情况的地理信息获取、处理、统计、分析和评价及自然资源调查监测等工作。是自然资源浙江省卫星应用技术中心、自然资源部地理国情监测重点实验室两大科创平台的依托单位，挂浙江省自然资源行政执法技术中心牌子。通过自然资源调查监测、自然资源所有者权益和自然资源信息化建设三大业务方向全面融入自然资源管理业务，积极打造省域空间治理数字化平台、自然资源三维立体时空数据库、全省卫星应用技术体系、自然资源调查监测技术体系、自然资源资产清查统计技术体系、自然资源行政执法技术体系，全方位支撑自然资源“两统一”职责履行。
``` 
'''

response = get_completion(prompt, model, stream)

