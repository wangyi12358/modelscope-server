
input_type = {
  "text": "text",
  "imageUrl": "imageUrl", # 图片
  "videoUrl": "videoUrl",
}

output_type = {
  "scores": "scores",
  "text": "text",
  "texts": "texts",
  "imageUrl": "imageUrl"
}

task_cv = [
  {
    "taskName": '单标签图像分类',
    "taskKey": 'image-classification',
    "taskDesc": '对图像中的不同特征根据类别进行区分',
    "models": [
      {
        "apiPath": "/cv/image/category",
        "name": "获取图片类目(中文)",
        "input": input_type.get("imageUrl"),
        "output": output_type.get("scores")
      }
    ]
  },
  {
    "taskName": '通用图像分割',
    "taskKey": 'image-segmentation',
    "taskDesc": '识别图像主体与图像背景进行分离'
  },
  {
    "taskName": '文字检测',
    "taskKey": 'ocr-detection',
    "taskDesc": '将图像中的文字检测出来并返回检测点坐标位置',
    "models": [
      {
        "apiPath": "/cv/image/words",
        "name": "获取图片文字(中英文)",
        "input": input_type.get("imageUrl"),
        "output": output_type.get("texts")
      }
    ]
  },
  {
    "taskName": '人像美肤',
    "taskKey": 'skin-retouching',
    "taskDesc": '对图像中的人像皮肤进行细节美化'
  },
  {
    "taskName": '风格迁移',
    "taskKey": 'image-style-transfer',
    "taskDesc": '对图像或视频的色彩风格进行另一种风格转化'
  },
  {
    "taskName": '图像翻译',
    "taskKey": 'image-to-image-translation',
    "taskDesc": '将一张图片上的文字翻译成目标语言并生成新的图片'
  },
  {
    "taskName": '以图生图',
    "taskKey": 'image-to-image-generation',
    "taskDesc": '根据输入图像生成新的类似图像'
  },
  {
    "taskName": '搜索推荐',
    "taskKey": 'image-search',
    "taskDesc": '根据输入图像进行范围匹配'
  },
  {
    "taskName": '审核评估',
    "taskKey": 'image-evaluation',
    "taskDesc": '对图像进行解析并自动给出一个评估信息'
  },
  {
    "taskName": '视频处理',
    "taskKey": 'video-processing',
    "taskDesc": '对视频信息进行自动运算处理'
  },
  {
    "taskName": '视频检测',
    "taskKey": 'video-detecction',
    "taskDesc": '对视频信息进行内容解析'
  },
  {
    "taskName": '视频分割',
    "taskKey": 'video-segmentation',
    "taskDesc": '对视频信息进行背景和主体分离'
  },
  {
    "taskName": '视频生成',
    "taskKey": 'video-generation',
    "taskDesc": '对视频进行解析匹配视频信息进行生成'
  },
  {
    "taskName": '视频编辑',
    "taskKey": 'video-editing',
    "taskDesc": '对视频进行解析转化为可编辑状态'
  },
  {
    "taskName": '视频表征',
    "taskKey": 'video-embedding',
    "taskDesc": '对视频特征进行多模态匹配'
  },
  {
    "taskName": '视频检索',
    "taskKey": 'video-search',
    "taskDesc": '对视频解析根据规则提取部分信息'
  },
  {
    "taskName": '视频审核评估',
    "taskKey": 'video-evaluation',
    "taskDesc": '根据规则对视频解析并给出评估结果'
  },
  {
    "taskName": '视频文本识别',
    "taskKey": 'video-ocr',
    "taskDesc": '对视频中的文字内容进行识别'
  },
  {
    "taskName": '视频到文本',
    "taskKey": 'video-captioning',
    "taskDesc": '将视频中的音频转化为文本信息'
  },
  {
    "taskName": '三维重建',
    "taskKey": '3d-reconstruction',
    "taskDesc": '对三维模型解析并重新构建'
  },
  {
    "taskName": '三维识别',
    "taskKey": '3d-recognition',
    "taskDesc": '对三维模型进行识别并进行标注'
  },
  {
    "taskName": '三维编辑',
    "taskKey": '3d-editing',
    "taskDesc": '对三维模型解析转化为可编辑状态'
  },
  {
    "taskName": '驱动交互',
    "taskKey": '3d-driven',
    "taskDesc": '对三维模型解析转为为动态效果'
  },
  {
    "taskName": '渲染呈现',
    "taskKey": '3d-rendering',
    "taskDesc": '对三维模型进行渲染并以图像展示'
  },
  {
    "taskName": '虚拟试衣',
    "taskKey": 'virtual-try-on',
    "taskDesc": '给定模特图片和衣服图片，合成模特穿上给定衣服的图片'
  },
  {
    "taskName": '文字识别',
    "taskKey": 'ocr-recognition',
    "taskDesc": '将图像中的文字识别出来并返回文本内容'
  },
  {
    "taskName": '人脸检测',
    "taskKey": 'face-detection',
    "taskDesc": '对图像中的人脸进行检测并返回人脸坐标位置'
  },
  {
    "taskName": '人脸识别',
    "taskKey": 'face-recognition',
    "taskDesc": '对矫正对齐后的人脸图像提取特征向量'
  },
  {
    "taskName": '人体检测',
    "taskKey": 'human-detection',
    "taskDesc": '对图像中的人体关键点进行检测并返回关键点标签与坐标位置'
  },
  {
    "taskName": '人物交互关系',
    "taskKey": 'human-object-interaction',
    "taskDesc": '对图像中的肢体关键点和物品进行检测和识别对坐标信息进行处理'
  },
  {
    "taskName": '人脸生成',
    "taskKey": 'face-image-generation',
    "taskDesc": '对图像中的人脸进行区域位置检测并生成虚拟人脸'
  },
  {
    "taskName": '多标签图像分类',
    "taskKey": 'image-multilabel-classification',
    "taskDesc": '解析图像特征支持多个类别区分'
  },
  {
    "taskName": '通用目标检测',
    "taskKey": 'image-object-detection',
    "taskDesc": '对输入图像中的较通用物体定位及类别判断'
  },
  {
    "taskName": '目标检测-自动驾驶场景(行人、车辆、交通标注等)',
    "taskKey": 'image-object-detection-autopilot',
    "taskDesc": '对自动驾驶中的场景进行目标检测，图像中的人、车辆及交通信息等进行实时解析并进行标注（行人、车辆、交通标注）'
  },
  {
    "taskName": '目标检测-自动驾驶场景(车道线)',
    "taskKey": 'image-object-detection-laneline',
    "taskDesc": '对自动驾驶中的场景进行目标检测，图像中的人、车辆及交通信息等进行实时解析并进行标注（车道线）'
  },
  {
    "taskName": '人像抠图',
    "taskKey": 'portrait-matting',
    "taskDesc": '对输入的图像将人体部分抠出并对背景进行透明化处理'
  },
  {
    "taskName": '人像增强',
    "taskKey": 'image-portrait-enhancement',
    "taskDesc": '对图像中的人像主体进行细节增强'
  },
  {
    "taskName": '图像超分辨',
    "taskKey": 'image-super-resolution',
    "taskDesc": '对图像进行倍数放大且不丢失画面质量'
  },
  {
    "taskName": '图像上色',
    "taskKey": 'image-colorization',
    "taskDesc": '对黑白图像进行区域解析并对其进行类别上色'
  },
  {
    "taskName": '图像颜色增强',
    "taskKey": 'image-color-enhancement',
    "taskDesc": '对图像中色彩值进行解析并对其进行规则处理'
  },
  {
    "taskName": '图像降噪',
    "taskKey": 'image-denoising',
    "taskDesc": '对图像中的噪点进行处理降低'
  },
  {
    "taskName": '人像卡通化',
    "taskKey": 'image-portrait-stylization',
    "taskDesc": '对输入的图像进行卡通化处理，实现风格变化',
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
    "taskName": '图像表征',
    "taskKey": 'image-embedding',
    "taskDesc": '对输入图像特征进行多模态匹配'
  },
  {
    "taskName": '获取视频商品类目',
    "taskKey": 'live-category',
    "taskDesc": '实时解析识别直播画面中的商品类别进行信息展示',
    "models": [
      {
        "apiPath": "/cv/video/category",
        "name": "直播商品类目识别模型-中文-电商领域",
        "input": input_type.get("videoUrl"),
        "output": output_type.get("scores")
      }
    ]
  },
  {
    "taskName": '行为识别',
    "taskKey": 'action-recognition',
    "taskDesc": '对视频中的动作行为进行识别并返回类型'
  },
  {
    "taskName": '短视频内容分类',
    "taskKey": 'video-category',
    "taskDesc": '解析短视频语义进行场景分类',
    "models": [
      {
        "apiPath": "/cv/short/video/category",
        "name": "短视频内容分类模型-中文-通用领域",
        "input": input_type.get("videoUrl"),
        "output": output_type.get("scores")
      }
    ]
  },
  {
    "taskName": '目标跟踪及重识别',
    "taskKey": 'reid-and-tracking',
    "taskDesc": '可对图片和视频进行目标识别可重复识别'
  },
  {
    "taskName": '增强/虚拟现实',
    "taskKey": 'ar-vr',
    "taskDesc": '对vr图像信息进行画面增强'
  },
  {
    "taskName": '人体2D关键点',
    "taskKey": 'body-2d-keypoints',
    "taskDesc": '检测图像中人体2D关键点位置'
  },
  {
    "taskName": '商品图片特征',
    "taskKey": 'product-retrieval-embedding',
    "taskDesc": '对商品图像进行表征向量提取'
  },
  {
    "taskName": '视频场景分割',
    "taskKey": 'movie-scene-segmentation',
    "taskDesc": '输入一段长视频，算法将其分割成不同的场景子视频'
  },
  {
    "taskName": '人脸表情识别',
    "taskKey": 'facial-expression-recognition',
    "taskDesc": '识别图像中人脸的表情'
  },
  {
    "taskName": '手部2D关键点',
    "taskKey": 'hand-2d-keypoints',
    "taskDesc": '检测图像中手部21点关键点坐标'
  },
  {
    "taskName": '视频摘要',
    "taskKey": 'video-summarization',
    "taskDesc": '输入一段长视频，算法找出其中的一些关键片段进行拼接，输出拼接的短的摘要视频'
  },
  {
    "taskName": '人脸2D关键点',
    "taskKey": 'face-2d-keypoints',
    "taskDesc": '检测图像中人脸106点关键点坐标和人脸朝向姿态角'
  },
  {
    "taskName": '行人重识别',
    "taskKey": 'image-reid-person',
    "taskDesc": '输入包含人的图片，输出图片的特征向量'
  },
  {
    "taskName": '3D人体关键点',
    "taskKey": 'body-3d-keypoints',
    "taskDesc": '检测视频中人体姿态的3D关键点坐标'
  },
  {
    "taskName": '视频单目标跟踪',
    "taskKey": 'video-single-object-tracking',
    "taskDesc": '输入视频和第一帧目标位置，在所有视频帧中预测该目标位置'
  },
  {
    "taskName": '行为检测',
    "taskKey": 'action-detection',
    "taskDesc": '检测视频中发生的行为动作，并给出动作的时空位置'
  },
  {
    "taskName": '人群密度估计',
    "taskKey": 'crowd-counting',
    "taskDesc": '输入一张图片，输出图片内有多少人'
  },
  {
    "taskName": '卡证检测矫正',
    "taskKey": 'card-detection',
    "taskDesc": '检测输入图片中是否存在卡证，并定位其角点，根据角点将卡证矫正为正视图'
  },
  {
    "taskName": '全身关键点检测',
    "taskKey": 'human-wholebody-keypoint',
    "taskDesc": '检测图片中全身关键点坐标，包括人脸关键点，骨骼关键点、脚步关键点和手势关键点，共计133点'
  },
  {
    "taskName": '视频目标检测',
    "taskKey": 'video-object-detection',
    "taskDesc": '任务的输入输出类型及数据格式'
  },
  {
    "taskName": '语义分割',
    "taskKey": 'semantic-segmentation',
    "taskDesc": '图像显著性，预测图中每个像素的重要程度'
  },
  {
    "taskName": '人体美型',
    "taskKey": 'image-body-reshaping',
    "taskDesc": '给定一张人物图像（半身或全身），无需任何额外输入，端到端地实现对人物身体区域（肩部，腰部，腿部等）的自动化美型处理'
  },
  {
    "taskName": '目标检测-自动驾驶场景',
    "taskKey": 'image-object-detection-auto',
    "taskDesc": '检测自动驾驶场景图片的目标，包括车辆，行人等'
  },
  {
    "taskName": '图像填充',
    "taskKey": 'image-inpainting',
    "taskDesc": '输入一张图片；同时用户根据该图片，自定义地可以进行在线绘制任意形状的mask；最终输出恢复、补全后的图像'
  },
  {
    "taskName": '视频修复',
    "taskKey": 'video-inpainting',
    "taskDesc": '对视频中指定的区域和帧范围，进行视频修复'
  },
  {
    "taskName": '2D手势语义识别',
    "taskKey": 'hand-static',
    "taskDesc": '对图片中的人手动作的语义进行识别'
  },
  {
    "taskName": '人脸情绪识别',
    "taskKey": 'face-emotion',
    "taskDesc": '对图片中的人的情绪进行识别'
  },
  {
    "taskName": '人脸人体人手三合一检测',
    "taskKey": 'face-human-hand-detection',
    "taskDesc": '对图片中的人脸、人体、人手进行检测'
  },
  {
    "taskName": '通用商品分割',
    "taskKey": 'product-segmentation',
    "taskDesc": '对图片中的商品进行分割'
  },
  {
    "taskName": '商品显著性分割',
    "taskKey": 'shop-segmentation',
    "taskDesc": '对商品图像进行显著性分割'
  },
  {
    "taskName": '文本指导的图像分割',
    "taskKey": 'text-driven-segmentation',
    "taskDesc": '根据文本对图像进行分割'
  },
  {
    "taskName": '动物识别',
    "taskKey": 'animal-recognition',
    "taskDesc": '对图片中的动物主体的进行识别'
  },
  {
    "taskName": '视频文本表征',
    "taskKey": 'video-multi-modal-embedding',
    "taskDesc": '输入任意视频和文本pair，输出相应的视频-文本pair特征，和相应得分'
  },
  {
    "taskName": '自然语言引导的视频摘要',
    "taskKey": 'language-guided-video-summarization',
    "taskDesc": '输入一段长视频和N句英文描述，算法找出其中和英文描述相关的一些关键片段进行拼接，输出拼接的短的摘要视频'
  },
  {
    "taskName": '文本指导的视频目标分割',
    "taskKey": 'referring-video-object-segmentation',
    "taskDesc": '通过用户输入的文本描述（英文）从输入视频中分割出指定的物体，支持一次性输入两个物体描述'
  },
  {
    "taskName": '万物识别',
    "taskKey": 'general-recognition',
    "taskDesc": '对图片中的物体主体的进行识别'
  }
]

task_nlp = [
  {
    "taskName": "分词",
    "taskKey": "word-segmentation",
    "taskDesc": "分词，将连续的自然语言文本，切分成具有语义合理性和完整性的词汇序列"
  }, {
    "taskName": "命名实体识别",
    "taskKey": "named-entity-recognition",
    "taskDesc": "指识别自然语言文本中具有特定意义的实体，通用领域如人名、地名、机构名等",
    "models": [
      {
        "apiPath": "/nlp/entity",
        "name": "命名实体识别-英语-电商领域-large",
        "input": input_type.get("text"),
        "output": output_type.get("scores"),
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
    "taskName": "词性标注",
    "taskKey": "part-of-speech",
    "taskDesc": "指为自然语言文本中的每个词汇赋予一个词性的过程，如名词、动词、副词等"
  }, {
    "taskName": "文本向量",
    "taskKey": "sentence-embedding",
    "taskDesc": "将输入文本从字符转化成向量表示"
  }, {
    "taskName": "语义相关性",
    "taskKey": "text-ranking",
    "taskDesc": "给出大量的候选段落，然后再给一个问题，模型从大量的候选段落找出能回答问题的那个段落"
  }, {
    "taskName": "文本分割",
    "taskKey": "document-segmentation",
    "taskDesc": "对于口语识别的长文本数据，使用文本段落分割模型来提升转写结果的可读性；同时也可用于书面化长文本的分段修正。"
  }, {
    "taskName": "文本纠错",
    "taskKey": "text-error-correction",
    "taskDesc": "准确识别输入文本中出现的拼写错别字及其段落位置信息，并针对性给出正确的建议文本内容"
  }, {
    "taskName": "文本分类",
    "taskKey": "text-classification",
    "taskDesc": "模型将载有信息的一篇文本映射到预先给定的某一类别或某几类别主题的过程"
  }, {
    "taskName": "情感分类",
    "taskKey": "sentiment-classification",
    "taskDesc": "分析并给出文本的情感正负倾向"
  }, {
    "taskName": "句子相似度",
    "taskKey": "sentence-similarity",
    "taskDesc": "文本相似度服务提供不同文本之间相似度的计算，并输出一个介于0到1之间的分数，分数越大则文本之间的相似度越高"
  }, {
    "taskName": "零样本分类",
    "taskKey": "zero-shot-classification",
    "taskDesc": "只需要提供待分类的句子和类别标签即可给出句子类别"
  }, {
    "taskName": "自然语言推理",
    "taskKey": "nli",
    "taskDesc": "判断两个句子（Premise, Hypothesis）或者两个词之间的语义关系"
  }, {
    "taskName": "问答",
    "taskKey": "question-answering",
    "taskDesc": "给定一长段文字，然后再给一个问题，然后理解长段文字之后，对这个问题进行解答。"
  }, {
    "taskName": "任务型对话",
    "taskKey": "task-oriented-conversation",
    "taskDesc": "主要指机器人为满足用户某一需求而产生的多轮对话，机器人通过理解、澄清等方式确定用户意图，继而通过答复、调用API等方式完成该任务"
  }, {
    "taskName": "开放型对话",
    "taskKey": "open-domain-conversation",
    "taskDesc": "无目的、无领域约束能够在开放域内进行有意义的对话"
  }, {
    "taskName": "FAQ问答",
    "taskKey": "faq-question-answering",
    "taskDesc": "输入候选FAQ列表和一个或多个query，模型输出排序后的FAQ列表"
  }, {
    "taskName": "表格问答",
    "taskKey": "table-question-answering",
    "taskDesc": "给定一张表格和一个query，query是询问表格里面的一些信息，模型给出答案"
  }, {
    "taskName": "翻译",
    "taskKey": "translation",
    "taskDesc": "将一种语言的文本翻译成指定语言的文本",
    "models": [
      {
        "apiPath": "/nlp/translation",
        "name": "中英文翻译",
        "input": input_type.get("text"),
        "output": output_type.get("text")
      }
    ]
  }, {
    "taskName": "完形填空",
    "taskKey": "fill-mask",
    "taskDesc": "输入一段文本，同时将里面的部分词mask掉，模型通过理解上下文预测被mask的词"
  }, {
    "taskName": "文本生成",
    "taskKey": "text-generation",
    "taskDesc": "模型接受各种形式的信息作为输入，包括文本或者非文本结构化信息等，生成可读的文字表述。",
    "models": [
      {
        "apiPath": "/nlp/generate/product/desc",
        "name": "PALM商品文案描述生成介绍",
        "input": input_type.get("text"),
        "output": output_type.get("text")
      }
    ]
  }, {
    "taskName": "文本摘要",
    "taskKey": "text-summarization",
    "taskDesc": "自动抽取输入文本中的关键信息并生成指定长度的摘要"
  }, {
    "taskName": "生成文本质量评价",
    "taskKey": "generation-quality-evaluation",
    "taskDesc": "在给定源端输入、目标端参考答案、或两者均有提供的情况下，算法用于评估所生成文本的质量"
  }, {
    "taskName": "端到端文本生成",
    "taskKey": "text2text-generation",
    "taskDesc": "模型encoder端通过对输入信息进行理解编码后，在decoder端将信息解码生成可读的文字表述"
  }, {
    "taskName": "特征抽取",
    "taskKey": "feature-extraction",
    "taskDesc": "通过模型将原始输入数据转化为向量特征"
  }, {
    "taskName": "关系抽取",
    "taskKey": "relation-extraction",
    "taskDesc": "非结构或半结构化数据中找出主体与客体之间存在的关系，并将其表示为实体关系三元组"
  }]

task_multi_modal = [
  {
    "taskName": "图像描述",
    "taskKey": "image-captioning",
    "taskDesc": "根据图片生成一段文本描述",
    "models": [
      {
        "apiPath": "/multi/modal/image/caption",
        "name": "图像描述-中文-电商领域",
        "input": input_type.get("imageUrl"),
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