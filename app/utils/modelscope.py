from enum import Enum

input_type = {
    "text": "text",
    "imageUrl": "imageUrl",  # 图片
    "videoUrl": "videoUrl",
    "switch": "switch"
}

output_type = {
    "scores": "scores",
    "text": "text",
    "texts": "texts",
    "spans": "spans",
    "imageUrl": "imageUrl"
}


class LanguageEnum(Enum):
    zh_CN = "zh_CN"
    en_US = "en_US"


task_cv = [
    {
        "name": '单标签图像分类',
        "key": 'image-classification',
        "desc": '对图像中的不同特征根据类别进行区分',
        "models": [
            {
                "apiPath": "/cv/image/category",
                "name": "获取图片类目",
                "input": input_type.get("imageUrl"),
                "languages": [LanguageEnum.zh_CN.value],
                "output": output_type.get("scores")
            }
        ]
    },
    {
        "name": '通用图像分割',
        "key": 'image-segmentation',
        "desc": '识别图像主体与图像背景进行分离'
    },
    {
        "name": '文字检测',
        "key": 'ocr-detection',
        "desc": '将图像中的文字检测出来并返回检测点坐标位置',
        "models": [
            {
                "apiPath": "/cv/image/words",
                "name": "获取图片文字",
                "input": input_type.get("imageUrl"),
                "languages": [LanguageEnum.zh_CN.value, LanguageEnum.en_US.value],
                "output": output_type.get("texts")
            }
        ]
    },
    {
        "name": '人像美肤',
        "key": 'skin-retouching',
        "desc": '对图像中的人像皮肤进行细节美化'
    },
    {
        "name": '风格迁移',
        "key": 'image-style-transfer',
        "desc": '对图像或视频的色彩风格进行另一种风格转化'
    },
    {
        "name": '图像翻译',
        "key": 'image-to-image-translation',
        "desc": '将一张图片上的文字翻译成目标语言并生成新的图片'
    },
    {
        "name": '以图生图',
        "key": 'image-to-image-generation',
        "desc": '根据输入图像生成新的类似图像'
    },
    {
        "name": '搜索推荐',
        "key": 'image-search',
        "desc": '根据输入图像进行范围匹配'
    },
    {
        "name": '审核评估',
        "key": 'image-evaluation',
        "desc": '对图像进行解析并自动给出一个评估信息'
    },
    {
        "name": '视频处理',
        "key": 'video-processing',
        "desc": '对视频信息进行自动运算处理'
    },
    {
        "name": '视频检测',
        "key": 'video-detecction',
        "desc": '对视频信息进行内容解析'
    },
    {
        "name": '视频分割',
        "key": 'video-segmentation',
        "desc": '对视频信息进行背景和主体分离'
    },
    {
        "name": '视频生成',
        "key": 'video-generation',
        "desc": '对视频进行解析匹配视频信息进行生成'
    },
    {
        "name": '视频编辑',
        "key": 'video-editing',
        "desc": '对视频进行解析转化为可编辑状态'
    },
    {
        "name": '视频表征',
        "key": 'video-embedding',
        "desc": '对视频特征进行多模态匹配'
    },
    {
        "name": '视频检索',
        "key": 'video-search',
        "desc": '对视频解析根据规则提取部分信息'
    },
    {
        "name": '视频审核评估',
        "key": 'video-evaluation',
        "desc": '根据规则对视频解析并给出评估结果'
    },
    {
        "name": '视频文本识别',
        "key": 'video-ocr',
        "desc": '对视频中的文字内容进行识别'
    },
    {
        "name": '视频到文本',
        "key": 'video-captioning',
        "desc": '将视频中的音频转化为文本信息'
    },
    {
        "name": '三维重建',
        "key": '3d-reconstruction',
        "desc": '对三维模型解析并重新构建'
    },
    {
        "name": '三维识别',
        "key": '3d-recognition',
        "desc": '对三维模型进行识别并进行标注'
    },
    {
        "name": '三维编辑',
        "key": '3d-editing',
        "desc": '对三维模型解析转化为可编辑状态'
    },
    {
        "name": '驱动交互',
        "key": '3d-driven',
        "desc": '对三维模型解析转为为动态效果'
    },
    {
        "name": '渲染呈现',
        "key": '3d-rendering',
        "desc": '对三维模型进行渲染并以图像展示'
    },
    {
        "name": '虚拟试衣',
        "key": 'virtual-try-on',
        "desc": '给定模特图片和衣服图片，合成模特穿上给定衣服的图片'
    },
    {
        "name": '文字识别',
        "key": 'ocr-recognition',
        "desc": '将图像中的文字识别出来并返回文本内容'
    },
    {
        "name": '人脸检测',
        "key": 'face-detection',
        "desc": '对图像中的人脸进行检测并返回人脸坐标位置'
    },
    {
        "name": '人脸识别',
        "key": 'face-recognition',
        "desc": '对矫正对齐后的人脸图像提取特征向量'
    },
    {
        "name": '人体检测',
        "key": 'human-detection',
        "desc": '对图像中的人体关键点进行检测并返回关键点标签与坐标位置'
    },
    {
        "name": '人物交互关系',
        "key": 'human-object-interaction',
        "desc": '对图像中的肢体关键点和物品进行检测和识别对坐标信息进行处理'
    },
    {
        "name": '人脸生成',
        "key": 'face-image-generation',
        "desc": '对图像中的人脸进行区域位置检测并生成虚拟人脸',
        "models": [
            {
                "apiPath": "/cv/generation/face",
                "name": "人脸生成",
                # "input": input_type.get("switch"),
                "output": output_type.get("imageUrl")
            }
        ]
    },
    {
        "name": '多标签图像分类',
        "key": 'image-multilabel-classification',
        "desc": '解析图像特征支持多个类别区分'
    },
    {
        "name": '通用目标检测',
        "key": 'image-object-detection',
        "desc": '对输入图像中的较通用物体定位及类别判断'
    },
    {
        "name": '目标检测-自动驾驶场景(行人、车辆、交通标注等)',
        "key": 'image-object-detection-autopilot',
        "desc": '对自动驾驶中的场景进行目标检测，图像中的人、车辆及交通信息等进行实时解析并进行标注（行人、车辆、交通标注）'
    },
    {
        "name": '目标检测-自动驾驶场景(车道线)',
        "key": 'image-object-detection-laneline',
        "desc": '对自动驾驶中的场景进行目标检测，图像中的人、车辆及交通信息等进行实时解析并进行标注（车道线）'
    },
    {
        "name": '人像抠图',
        "key": 'portrait-matting',
        "desc": '对输入的图像将人体部分抠出并对背景进行透明化处理'
    },
    {
        "name": '人像增强',
        "key": 'image-portrait-enhancement',
        "desc": '对图像中的人像主体进行细节增强'
    },
    {
        "name": '图像超分辨',
        "key": 'image-super-resolution',
        "desc": '对图像进行倍数放大且不丢失画面质量'
    },
    {
        "name": '图像上色',
        "key": 'image-colorization',
        "desc": '对黑白图像进行区域解析并对其进行类别上色'
    },
    {
        "name": '图像颜色增强',
        "key": 'image-color-enhancement',
        "desc": '对图像中色彩值进行解析并对其进行规则处理'
    },
    {
        "name": '图像降噪',
        "key": 'image-denoising',
        "desc": '对图像中的噪点进行处理降低'
    },
    {
        "name": '人像卡通化',
        "key": 'image-portrait-stylization',
        "desc": '对输入的图像进行卡通化处理，实现风格变化',
        "models": [
            {
                "apiPath": "/cv/image/cartoon/3d",
                "name": "根据人像图片获取3d图片",
                "input": input_type.get("imageUrl"),
                "output": output_type.get("imageUrl")
            }
        ]
    },
    {
        "name": '图像表征',
        "key": 'image-embedding',
        "desc": '对输入图像特征进行多模态匹配'
    },
    {
        "name": '获取视频商品类目',
        "key": 'live-category',
        "desc": '实时解析识别直播画面中的商品类别进行信息展示',
        "models": [
            {
                "apiPath": "/cv/video/category",
                "name": "直播商品类目识别模型-电商领域",
                "input": input_type.get("videoUrl"),
                "languages": [LanguageEnum.zh_CN.value],
                "output": output_type.get("scores")
            }
        ]
    },
    {
        "name": '行为识别',
        "key": 'action-recognition',
        "desc": '对视频中的动作行为进行识别并返回类型'
    },
    {
        "name": '短视频内容分类',
        "key": 'video-category',
        "desc": '解析短视频语义进行场景分类',
        "models": [
            {
                "apiPath": "/cv/short/video/category",
                "name": "短视频内容分类模型-通用领域",
                "input": input_type.get("videoUrl"),
                "languages": [LanguageEnum.zh_CN.value],
                "output": output_type.get("scores")
            }
        ]
    },
    {
        "name": '目标跟踪及重识别',
        "key": 'reid-and-tracking',
        "desc": '可对图片和视频进行目标识别可重复识别'
    },
    {
        "name": '增强/虚拟现实',
        "key": 'ar-vr',
        "desc": '对vr图像信息进行画面增强'
    },
    {
        "name": '人体2D关键点',
        "key": 'body-2d-keypoints',
        "desc": '检测图像中人体2D关键点位置'
    },
    {
        "name": '商品图片特征',
        "key": 'product-retrieval-embedding',
        "desc": '对商品图像进行表征向量提取'
    },
    {
        "name": '视频场景分割',
        "key": 'movie-scene-segmentation',
        "desc": '输入一段长视频，算法将其分割成不同的场景子视频'
    },
    {
        "name": '人脸表情识别',
        "key": 'facial-expression-recognition',
        "desc": '识别图像中人脸的表情'
    },
    {
        "name": '手部2D关键点',
        "key": 'hand-2d-keypoints',
        "desc": '检测图像中手部21点关键点坐标'
    },
    {
        "name": '视频摘要',
        "key": 'video-summarization',
        "desc": '输入一段长视频，算法找出其中的一些关键片段进行拼接，输出拼接的短的摘要视频'
    },
    {
        "name": '人脸2D关键点',
        "key": 'face-2d-keypoints',
        "desc": '检测图像中人脸106点关键点坐标和人脸朝向姿态角'
    },
    {
        "name": '行人重识别',
        "key": 'image-reid-person',
        "desc": '输入包含人的图片，输出图片的特征向量'
    },
    {
        "name": '3D人体关键点',
        "key": 'body-3d-keypoints',
        "desc": '检测视频中人体姿态的3D关键点坐标'
    },
    {
        "name": '视频单目标跟踪',
        "key": 'video-single-object-tracking',
        "desc": '输入视频和第一帧目标位置，在所有视频帧中预测该目标位置'
    },
    {
        "name": '行为检测',
        "key": 'action-detection',
        "desc": '检测视频中发生的行为动作，并给出动作的时空位置'
    },
    {
        "name": '人群密度估计',
        "key": 'crowd-counting',
        "desc": '输入一张图片，输出图片内有多少人'
    },
    {
        "name": '卡证检测矫正',
        "key": 'card-detection',
        "desc": '检测输入图片中是否存在卡证，并定位其角点，根据角点将卡证矫正为正视图'
    },
    {
        "name": '全身关键点检测',
        "key": 'human-wholebody-keypoint',
        "desc": '检测图片中全身关键点坐标，包括人脸关键点，骨骼关键点、脚步关键点和手势关键点，共计133点'
    },
    {
        "name": '视频目标检测',
        "key": 'video-object-detection',
        "desc": '任务的输入输出类型及数据格式'
    },
    {
        "name": '语义分割',
        "key": 'semantic-segmentation',
        "desc": '图像显著性，预测图中每个像素的重要程度'
    },
    {
        "name": '人体美型',
        "key": 'image-body-reshaping',
        "desc": '给定一张人物图像（半身或全身），无需任何额外输入，端到端地实现对人物身体区域（肩部，腰部，腿部等）的自动化美型处理'
    },
    {
        "name": '目标检测-自动驾驶场景',
        "key": 'image-object-detection-auto',
        "desc": '检测自动驾驶场景图片的目标，包括车辆，行人等'
    },
    {
        "name": '图像填充',
        "key": 'image-inpainting',
        "desc": '输入一张图片；同时用户根据该图片，自定义地可以进行在线绘制任意形状的mask；最终输出恢复、补全后的图像'
    },
    {
        "name": '视频修复',
        "key": 'video-inpainting',
        "desc": '对视频中指定的区域和帧范围，进行视频修复'
    },
    {
        "name": '2D手势语义识别',
        "key": 'hand-static',
        "desc": '对图片中的人手动作的语义进行识别'
    },
    {
        "name": '人脸情绪识别',
        "key": 'face-emotion',
        "desc": '对图片中的人的情绪进行识别'
    },
    {
        "name": '人脸人体人手三合一检测',
        "key": 'face-human-hand-detection',
        "desc": '对图片中的人脸、人体、人手进行检测'
    },
    {
        "name": '通用商品分割',
        "key": 'product-segmentation',
        "desc": '对图片中的商品进行分割'
    },
    {
        "name": '商品显著性分割',
        "key": 'shop-segmentation',
        "desc": '对商品图像进行显著性分割'
    },
    {
        "name": '文本指导的图像分割',
        "key": 'text-driven-segmentation',
        "desc": '根据文本对图像进行分割'
    },
    {
        "name": '动物识别',
        "key": 'animal-recognition',
        "desc": '对图片中的动物主体的进行识别'
    },
    {
        "name": '视频文本表征',
        "key": 'video-multi-modal-embedding',
        "desc": '输入任意视频和文本pair，输出相应的视频-文本pair特征，和相应得分'
    },
    {
        "name": '自然语言引导的视频摘要',
        "key": 'language-guided-video-summarization',
        "desc": '输入一段长视频和N句英文描述，算法找出其中和英文描述相关的一些关键片段进行拼接，输出拼接的短的摘要视频'
    },
    {
        "name": '文本指导的视频目标分割',
        "key": 'referring-video-object-segmentation',
        "desc": '通过用户输入的文本描述（英文）从输入视频中分割出指定的物体，支持一次性输入两个物体描述'
    },
    {
        "name": '万物识别',
        "key": 'general-recognition',
        "desc": '对图片中的物体主体的进行识别'
    }
]

task_nlp = [
    {
        "name": "分词",
        "key": "word-segmentation",
        "desc": "分词，将连续的自然语言文本，切分成具有语义合理性和完整性的词汇序列"
    }, {
        "name": "命名实体识别",
        "key": "named-entity-recognition",
        "desc": "指识别自然语言文本中具有特定意义的实体，通用领域如人名、地名、机构名等",
        "models": [
            {
                "apiPath": "/nlp/entity",
                "name": "命名实体识别-电商领域",
                "input": input_type.get("text"),
                "output": output_type.get("spans"),
                "languages": [LanguageEnum.en_US.value],
                "samples": [
                    'I typically camp remotely in the back country and this will be great to bring along to keep devices charged when not driving and keep the kids power hungry tablets/iPads that we let them watch at night in the tent and during boring parts of the drive.',
                    'I just used it this weekend to power my Alpicool mini fridge on our road trip and was extremely satisfied with how well it worked and how long it lasted.',
                    'This little guy is great for camping, running fans, etc at the picnic table in the summer, charging devices, etc.',
                    'I got this for my camping trips.',
                    'It was an easy decision to buy this for camping and my DC travel CPAP machine.',
                    'If all I do is use it for topping up phones and tablets by USB all week, it will stay at 99% and then switch off at zero.',
                    'I bought this for the small size and the Anker brand, the later being a mistake.',
                ],
            }
        ]
    }, {
        "name": "词性标注",
        "key": "part-of-speech",
        "desc": "指为自然语言文本中的每个词汇赋予一个词性的过程，如名词、动词、副词等"
    }, {
        "name": "文本向量",
        "key": "sentence-embedding",
        "desc": "将输入文本从字符转化成向量表示"
    }, {
        "name": "语义相关性",
        "key": "text-ranking",
        "desc": "给出大量的候选段落，然后再给一个问题，模型从大量的候选段落找出能回答问题的那个段落"
    }, {
        "name": "文本分割",
        "key": "document-segmentation",
        "desc": "对于口语识别的长文本数据，使用文本段落分割模型来提升转写结果的可读性；同时也可用于书面化长文本的分段修正。"
    }, {
        "name": "文本纠错",
        "key": "text-error-correction",
        "desc": "准确识别输入文本中出现的拼写错别字及其段落位置信息，并针对性给出正确的建议文本内容"
    }, {
        "name": "文本分类",
        "key": "text-classification",
        "desc": "模型将载有信息的一篇文本映射到预先给定的某一类别或某几类别主题的过程",
        "models": [
            {
                "apiPath": "/nlp/analysis",
                "name": "情感分析-英文",
                "input": input_type.get("text"),
                "languages": [LanguageEnum.en_US.value],
                "output": output_type.get("scores")
            }
        ]
    }, {
        "name": "情感分类",
        "key": "sentiment-classification",
        "desc": "分析并给出文本的情感正负倾向"
    }, {
        "name": "句子相似度",
        "key": "sentence-similarity",
        "desc": "文本相似度服务提供不同文本之间相似度的计算，并输出一个介于0到1之间的分数，分数越大则文本之间的相似度越高"
    },
    {
        "name": "零样本分类",
        "key": "zero-shot-classification",
        "desc": "只需要提供待分类的句子和类别标签即可给出句子类别"
    },
    {
        "name": "自然语言推理",
        "key": "nli",
        "desc": "判断两个句子（Premise, Hypothesis）或者两个词之间的语义关系"
    },
    {
        "name": "问答",
        "key": "question-answering",
        "desc": "给定一长段文字，然后再给一个问题，然后理解长段文字之后，对这个问题进行解答。"
    },
    {
        "name": "任务型对话",
        "key": "task-oriented-conversation",
        "desc": "主要指机器人为满足用户某一需求而产生的多轮对话，机器人通过理解、澄清等方式确定用户意图，继而通过答复、调用API等方式完成该任务"
    },
    {
        "name": "开放型对话",
        "key": "open-domain-conversation",
        "desc": "无目的、无领域约束能够在开放域内进行有意义的对话"
    },
    {
        "name": "FAQ问答",
        "key": "faq-question-answering",
        "desc": "输入候选FAQ列表和一个或多个query，模型输出排序后的FAQ列表"
    },
    {
        "name": "表格问答",
        "key": "table-question-answering",
        "desc": "给定一张表格和一个query，query是询问表格里面的一些信息，模型给出答案"
    },
    {
        "name": "翻译",
        "key": "translation",
        "desc": "将一种语言的文本翻译成指定语言的文本",
        "models": [
            {
                "apiPath": "/nlp/translation",
                "name": "中英文翻译",
                "input": input_type.get("text"),
                "languages": [LanguageEnum.en_US.value],
                "output": output_type.get("text")
            }
        ]
    },
    {
        "name": "完形填空",
        "key": "fill-mask",
        "desc": "输入一段文本，同时将里面的部分词mask掉，模型通过理解上下文预测被mask的词"
    },
    {
        "name": "文本生成",
        "key": "text-generation",
        "desc": "模型接受各种形式的信息作为输入，包括文本或者非文本结构化信息等，生成可读的文字表述。",
        "models": [
            {
                "apiPath": "/nlp/generate/product/desc",
                "name": "PALM商品文案描述生成介绍",
                "input": input_type.get("text"),
                "languages": [LanguageEnum.zh_CN.value],
                "output": output_type.get("text")
            }
        ]
    },
    {
        "name": "文本摘要",
        "key": "text-summarization",
        "desc": "自动抽取输入文本中的关键信息并生成指定长度的摘要",
        "models": [
            {
                "apiPath": "/nlp/summarization",
                "name": "多语言大模型-生成式摘要",
                "input": input_type.get("text"),
                "languages": [LanguageEnum.zh_CN.value],
                "output": output_type.get("text")
            }
        ]
    },
    {
        "name": "生成文本质量评价",
        "key": "generation-quality-evaluation",
        "desc": "在给定源端输入、目标端参考答案、或两者均有提供的情况下，算法用于评估所生成文本的质量"
    },
    {
        "name": "端到端文本生成",
        "key": "text2text-generation",
        "desc": "模型encoder端通过对输入信息进行理解编码后，在decoder端将信息解码生成可读的文字表述"
    },
    {
        "name": "特征抽取",
        "key": "feature-extraction",
        "desc": "通过模型将原始输入数据转化为向量特征"
    },
    {
        "name": "关系抽取",
        "key": "relation-extraction",
        "desc": "非结构或半结构化数据中找出主体与客体之间存在的关系，并将其表示为实体关系三元组"
    }
]

task_multi_modal = [
    {
        "name": "图像描述",
        "key": "image-captioning",
        "desc": "根据图片生成一段文本描述",
        "models": [
            {
                "apiPath": "/multi/modal/image/caption",
                "name": "图像描述-电商领域",
                "input": input_type.get("imageUrl"),
                "languages": [LanguageEnum.zh_CN.value],
                "output": output_type.get("text")
            }
        ]
    }
]

domain = {
    "nlp": {
        "name": '自然语言处理',
        "fullName": 'Natural Language Processing',
        "tasks": task_nlp
    },
    "cv": {
        "name": '计算机视觉',
        "fullName": 'Computer Vision',
        "tasks": task_cv
    },
    "multiModal": {
        "name": '多模态',
        "fullName": 'Multi-Modal',
        "tasks": task_multi_modal
    },
}
