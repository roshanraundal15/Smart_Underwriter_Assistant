
import FeatureCard from "@/components/FeatureCard";
import Header from "@/components/Header";
import WhyChooseUs from "@/components/WhyChooseUs";
import { useToast } from "@/hooks/use-toast";
import { Bot, Brain, MessageCircle, Rocket, Target, TrendingUp } from "lucide-react";

const Index = () => {
  const { toast } = useToast();

  const handleLaunchApp = (appName: string, url: string) => {
    toast({
      title: `Launching ${appName}`,
      description: `Opening ${appName} in a new window...`,
    });
    
    // In a real implementation, this would open the respective app
    window.open(url, '_blank');
  };

  const features = [
    {
      title: "🧠 Risk Profiling Engine",
      subtitle: "Intelligent Risk Evaluation & Decision Support",
      description: "Advanced algorithms to assess insurance applicant risk profiles using comprehensive lifestyle, medical, and financial data analysis.",
      features: [
        "Interactive assessment forms",
        "Multi-tier risk classification", 
        "5-year risk projection modeling",
        "Professional underwriter reports"
      ],
      buttonText: "Launch Assessment Tool",
      buttonIcon: Rocket,
      icon: Brain,
      gradient: "bg-gradient-to-r from-emerald-600 to-teal-600",
      url: "http://localhost:8501/"
    },
    {
      title: "🤖 AI Underwriter Chat", 
      subtitle: "Always-On Intelligent Insurance Guidance",
      description: "Sophisticated conversational AI providing real-time assistance for insurance eligibility, risk profiles, medical queries, and premium calculations.",
      features: [
        "Natural language processing",
        "Context-aware responses",
        "Medical & financial expertise", 
        "24/7 domain-specific support"
      ],
      buttonText: "Start AI Consultation",
      buttonIcon: Bot,
      icon: MessageCircle,
      gradient: "bg-gradient-to-r from-teal-600 to-cyan-600",
      url: "http://localhost:8503/"
    },
    {
      title: "💡 Personalized Recommendation Engine",
      subtitle: "Personalized Risk Improvement Strategies", 
      description: "Data-driven recommendations to enhance risk profiles and optimize insurance acceptance rates through targeted lifestyle and financial improvements.",
      features: [
        "Personalized health strategies",
        "Premium reduction pathways",
        "Condition-specific guidance",
        "Risk mitigation planning"
      ],
      buttonText: "Get Recommendation",
      buttonIcon: TrendingUp,
      icon: Target,
      gradient: "bg-gradient-to-r from-cyan-600 to-blue-600",
      url: "http://localhost:8502/"
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 via-white to-cyan-50">
      <Header />
      
      <div className="container mx-auto px-6 py-20">
        <div className="grid lg:grid-cols-3 gap-10 max-w-7xl mx-auto">
          {features.map((feature, index) => (
            <FeatureCard
              key={index}
              title={feature.title}
              subtitle={feature.subtitle} 
              description={feature.description}
              features={feature.features}
              buttonText={feature.buttonText}
              buttonIcon={feature.buttonIcon}
              icon={feature.icon}
              gradient={feature.gradient}
              onAction={() => handleLaunchApp(feature.title, feature.url)}
            />
          ))}
        </div>
      </div>

      <WhyChooseUs />
    </div>
  );
};

export default Index;
